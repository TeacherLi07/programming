/*
This code was written in pure C.
Build it with: (Windows only)
gcc ./mcping.c -o mcping.exe -lws2_32 -O2
MCPing v0.1.1
By Launium 2023. GitHub @layou233.
License: CC-BY-SA 3.0
*/

#include<stdio.h>
#include<stdlib.h>
#include<sys/timeb.h>
#include<winsock2.h>

typedef struct { 
  short sin_family; 
  u_short sin_port; 
  struct in_addr sin_addr; 
  char sin_zero[8]; 
} sockaddr_in;

boolean process_ip4(const char *ip, struct in_addr* addr)
{
    int dots = 0;
    int setions = 0;

    if (NULL == ip || *ip == '.') {
        return 0;
    }

    while (*ip) {
        if (*ip == '.') {
            if (setions >= 0 && setions <= 255) {
                *((&addr->S_un.S_un_b.s_b1)+dots) = setions;
                setions = 0;
                ip++;
                continue;
            }
            dots ++;
            return 0;
        }
        else if (*ip >= '0' && *ip <= '9') { // check if not a number
            setions = setions * 10 + (*ip - '0');
        } else
            return 0;
        ip++;
    }

    // check the last pattern
    if (setions >= 0 && setions <= 255) {
        if (dots == 3) {
            addr->S_un.S_un_b.s_b4 = setions;
            return 1;
        }
    }

    return 0;
}

int read_varint(const char* buf, int* numread) {
  int result = 0;
  int value;
  char byte;
  do {
    byte = *(buf++);
    value = byte & 0x7F;
    result |= value << (7 * *numread);

    (*numread)++;

    if (*numread > 5) {
      fprintf(stderr, "Error reading varint: varint too big\n");
      return -1;
    }
  } while ((byte & 0x80) != 0);

  return result;
}

void test_ping(sockaddr_in* addr, char* hostname, u_short le_port)
{
    SOCKET conn = socket(AF_INET, SOCK_STREAM, 0);
    if (INVALID_SOCKET == conn)
    {
        fprintf(stderr, "   Fail to initialize socket. Error: %d\n", WSAGetLastError());
        return;
    }
    int err = connect(conn, (struct sockaddr*)addr, sizeof(*addr));
    if (SOCKET_ERROR == err)
    {
        fprintf(stderr, "   Connection failed. Error: %d\n", WSAGetLastError());
        closesocket(conn);
        return;
    }

    char buf[1024];

    // generate status packet
    char hostname_len = strlen(hostname);
    char packet_len = 1; // packet ID
    packet_len += 1; // protocol version 47 (1.8.9)
    packet_len += 1; // hostname length
    packet_len += hostname_len; // hostname
    packet_len += 2; // little-endian port
    packet_len += 1; // next state

    char i = 0;
    buf[i++] = packet_len; // no need to encode varint
    buf[i++] = 0; // packet ID
    buf[i++] = 47;
    buf[i++] = hostname_len;
    memcpy(&buf[i], hostname, hostname_len);
    i += hostname_len;
    memcpy(&buf[i], &addr->sin_port, 2);
    i += 2;
    buf[i++] = 1;

    // append a empty packet for Status state
    buf[i++] = 1;
    buf[i++] = 0;

    err = send(conn, &buf[0], packet_len + 3, 0);
    if (err != packet_len + 3)
    {
        fprintf(stderr, "   Fail to write handshake packet. Error: %d\n", WSAGetLastError());
        closesocket(conn);
        return;
    }

    for (int read=0, to_recv; read < 5; read += err)
    {
        //printf("%d",to_recv);
        int to_recv = 5 - read;
        err = recv(conn, &buf[read], to_recv, 0);
        if (SOCKET_ERROR == err)
        {
            fprintf(stderr, "   Fail to read MOTD packet length. Error: %d, Read %d\n", WSAGetLastError(), read);
            closesocket(conn);
            return;
        }
    }
    int num_read = 0;
    int motd_len = read_varint(&buf[0], &num_read);
    if (motd_len == -1)
    {
        fprintf(stderr, "   Fail to read handshake response: got a strange VarInt number.\n");
        closesocket(conn);
        return;
    }
    motd_len -= 5 - num_read; // part of motd might be read already in this recv call
    // skip MOTD
    for (int read=0, to_recv; read < motd_len; read += err)
    {
        //printf("%d",to_recv);
        to_recv = motd_len - read;
        if (to_recv > 1024) to_recv = 1024;
        err = recv(conn, &buf[0], to_recv, 0);
        if (SOCKET_ERROR == err)
        {
            fprintf(stderr, "   Fail to read MOTD. Error: %d\n", WSAGetLastError());
            closesocket(conn);
            return;
        }
    }

    // send ping packet
    i = 0; // reset
    buf[i++] = 9; // packet length
    buf[i++] = 1; // packet ID
    struct timeb ping_time, pong_time;
    ftime(&ping_time);
    memcpy(&buf[i], &ping_time, sizeof(ping_time));
    err = send(conn, &buf[0], 10, 0);
    if (err != 10)
    {
        fprintf(stderr, "      Fail to write ping packet. Error: %d\n", WSAGetLastError());
        closesocket(conn);
        return;
    }

    // receive the first byte of pong packet
    err = recv(conn, &buf[0], 1, 0);
    ftime(&pong_time);
    closesocket(conn);
    if (err != 1)
    {
        fprintf(stderr, "   Fail to read pong packet. Error: %d\n", WSAGetLastError());
        return;
    }
    if (buf[0] != 9)
    {
        fprintf(stderr, "   Fail to read pong packet: unexpected pong packet length: %d\n", buf[0]);
        return;
    }
    u_int64 diff = pong_time.time * 1000 + pong_time.millitm - ping_time.time * 1000 - ping_time.millitm;
    printf("    Succeed. RTT=%llums\n", diff);
}

int main(int argc, char *argv[])
{
    printf("MCPing v0.1.1 Started...\n");
    if (argc < 2)
    {
        fprintf(stderr, "Bad usage. Example: ./mcping.exe mc.hypixel.net 25565 [-t]\n");
        return 1;
    }
    char *addr = argv[1];
    u_short port;
    if (argc == 3) port = 25565;
    else port = atoi(argv[2]);
    boolean t_mode = 0;
    if (argc > 3)
    {
        if (!strcmp(argv[3], "-t")) t_mode = 1;
    }
    
    WSADATA wsa;
    int err = WSAStartup(MAKEWORD(2, 2), &wsa);
    if (err != 0)
    {
        fprintf(stderr, "Fail to start up Winsock2! Error code: %d\n", err);
        return 1;
    }

    sockaddr_in s;
    s.sin_family = AF_INET;
    s.sin_port = htons(port);
    boolean is_domain = !process_ip4(addr, &s.sin_addr);
    if (is_domain)
    {
        HOSTENT *host_entry = gethostbyname(addr);
        if(NULL != host_entry)
        {
            s.sin_addr.S_un.S_un_b.s_b1 = host_entry->h_addr_list[0][0];
            s.sin_addr.S_un.S_un_b.s_b2 = host_entry->h_addr_list[0][1];
            s.sin_addr.S_un.S_un_b.s_b3 = host_entry->h_addr_list[0][2];
            s.sin_addr.S_un.S_un_b.s_b4 = host_entry->h_addr_list[0][3];
        } else {
            fprintf(stderr, "\nFail to resolve the hostname: %s\n", addr);
            return 1;
        }
    }

    printf("\nConnecting to tcp://%d.%d.%d.%d:%d using Minecraft JE Protocol Status...\n",
        s.sin_addr.S_un.S_un_b.s_b1,
        s.sin_addr.S_un.S_un_b.s_b2,
        s.sin_addr.S_un.S_un_b.s_b3,
        s.sin_addr.S_un.S_un_b.s_b4, port);

    if (t_mode) for (;;) test_ping(&s, addr, port);

    for (int n=0; n < 4; n++)
    {
        test_ping(&s, addr, port);
    }
    
    return 0;
}