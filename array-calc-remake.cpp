#include<bits/stdc++.h>
#include<winsock2.h>
#include<windows.h>
#include"json.hpp"
#include<curl/curl.h>
using namespace std;
using json = nlohmann::json;
const int N=10005;

string equa;
string modewd[3]={"","an=","sn="};
string version="1.3";
int mode;
double a[N],s[N],n;
bool iscalca[N],iscalcs[N];

string checkLatestRelease(const string &username, const string &repo)
{
    CURL *curl = curl_easy_init();
    if (!curl)
    {
        cerr << "Error: Failed to create cURL handle." << endl;
        return "";
    }

    string latestVersion;
    string url = "https://api.github.com/repos/" + username + "/" + repo + "/releases/latest";

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, [](char *data, size_t size, size_t nmemb, string *buffer) -> size_t {
        buffer->append(data, size * nmemb);
        return size * nmemb;
    });
    string response;
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);

    if (res != CURLE_OK)
    {
        cerr << "Error: Failed to send request. cURL error code: " << res << endl;
        return "";
    }

    try
    {
        json responseJson = json::parse(response);
        latestVersion = responseJson["tag_name"].get<string>();
    }
    catch (const json::parse_error &e)
    {
        cerr << "Error: Failed to parse response. JSON parse error: " << e.what() << endl;
    }

    return latestVersion;
}

void SetWindow(int Width, int Height, int WidthBuffer, int HeightBuffer) 
{ 
    _COORD coord; 
    coord.X = WidthBuffer; 
    coord.Y = HeightBuffer; 

    _SMALL_RECT Rect; 
    Rect.Top = 0; 
    Rect.Left = 0; 
    Rect.Bottom = Height - 1; 
    Rect.Right = Width - 1; 

    HANDLE Handle = GetStdHandle(STD_OUTPUT_HANDLE);      // Get Handle 
    SetConsoleScreenBufferSize(Handle, coord);            // Set Buffer Size 
    SetConsoleWindowInfo(Handle, TRUE, &Rect);            // Set Window Size 
}  // SetWindow

void initialize()
{
    system(("title ���м�����V"+version+" by TeacherLi").c_str());
    system("color f0");
    system("cls");
    SetWindow(120,30,120,2000);
    cout.setf(ios::fixed,ios::floatfield);
}

void printHelloPage()
{
    cout<<"========================================================================================================================"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                     ���м�����                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                    Version "<<version<<"                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                   ��д�ߣ�TeacherLi���Żԣ����ִ�����Դ��ChatGPT                                   ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                  https://github.com/TeacherLi07/Array-Calculator                                   ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                    ���س�������                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"========================================================================================================================";
    getchar();
}

void printInstructions()
{
    cout<<"========================================================================================================================"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   ʹ��˵����                                                                                                       ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   ����ʽ�ð�ǣ�Ӣ�ģ��ַ���ʾ��֧�ּӣ�+������-���ˣ�*������/���˷���^�����ݲ�֧�ָ��š�                          ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   ����ĳ����an��ʾ��ǰn�����sn��ʾ���������������Ϊ10000�                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   �����±�����ж����Ϊ�±�����š�                                                                             ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   �Ϸ�������磺an��a(n+1)��a((3n+5)^2)��a114��                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   �˷������У�ָ���͵�����ǵ���ĸ�����֣���Ҫ�����š�                                                           ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   ���ʽ��n��x�ȼۣ���Сд�����У���֧��С���������÷�����ʾ��                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   �������Ƿ������޷����㣬���ܻ��и�������ֵֹ����������ȷ���Ƿ�Ϊbug������ϵ�һ��ύissue��                 ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   ���س�������                                                                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"========================================================================================================================";
    getchar();
}

int main()
{
    initialize();  //��ʼ�����ڱ��⡢�ı�������ɫ�����ڴ�С�ͻ�������С
    printHelloPage();  //����ҳ
    system("cls");
    printInstructions();  //ʹ��˵��ҳ
    cout<<checkLatestRelease("TeacherLi07","Array_Calculator")<<endl;
}