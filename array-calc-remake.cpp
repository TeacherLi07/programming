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
    system(("title 数列计算器V"+version+" by TeacherLi").c_str());
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
    cout<<"||                                                     数列计算器                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                    Version "<<version<<"                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                   编写者：TeacherLi李信辉，部分代码来源于ChatGPT                                   ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                  https://github.com/TeacherLi07/Array-Calculator                                   ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                    按回车键继续                                                    ||"<<endl;
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
    cout<<"||   使用说明：                                                                                                       ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   代数式用半角（英文）字符表示，支持加（+）减（-）乘（*）除（/）乘方（^），暂不支持根号。                          ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   数列某项以an表示，前n项和以sn表示，计算总项数最大为10000项。                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   序数下标如果有多项，请为下标打括号。                                                                             ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   合法表达例如：an；a(n+1)；a((3n+5)^2)；a114。                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   乘方运算中，指数和底数如非单字母或纯数字，需要打括号。                                                           ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   表达式中n与x等价，大小写不敏感，不支持小数，可以用分数表示。                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   如果输入非法或者无法计算，可能会有各种奇奇怪怪的现象，如果不确定是否为bug可以联系我或提交issue。                 ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||   按回车键继续                                                                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"========================================================================================================================";
    getchar();
}

int main()
{
    initialize();  //初始化窗口标题、文本背景颜色、窗口大小和缓冲区大小
    printHelloPage();  //标题页
    system("cls");
    printInstructions();  //使用说明页
    cout<<checkLatestRelease("TeacherLi07","Array_Calculator")<<endl;
}