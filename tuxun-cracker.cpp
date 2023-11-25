#include <iostream>
#include <string>
#include <regex>
#include <cstdlib>
#include <Windows.h>


using namespace std;

string GetClipboardText() {
    string text;

    // 打开剪贴板
    if (OpenClipboard(NULL)) {
        // 获取剪贴板中的文本数据
        HANDLE hData = GetClipboardData(CF_TEXT);
        if (hData != NULL) {
            char* pszText = static_cast<char*>(GlobalLock(hData));
            if (pszText != NULL) {
                text = pszText;
                GlobalUnlock(hData);
            }
        }

        // 关闭剪贴板
        CloseClipboard();
    }

    return text;
}

int main() {
    while(1){
        // 收到回车时自动读取剪贴板内容
        cout << "按回车键自动读取剪贴板内容作为原始URL：" << endl;
        cin.ignore();  // 忽略回车键
        string input = GetClipboardText();

        // 使用正则表达式提取panoid的值
        regex panoidRegex("panoid=([^&]+)");
        smatch match;

        if (regex_search(input, match, panoidRegex)) {
            // 提取panoid的值
            string panoid = match[1].str();

            // 构建新的URL
            string newUrl = "https://www.google.com/maps/@?cbll=0,0&cbp=0,0,0,0,0&layer=c&panoid=" + panoid;
            cerr<<"new URL Done."<<endl;
            
            // 使用ShellExecute打开URL
            ShellExecuteA(NULL, "open", newUrl.c_str(), NULL, NULL, SW_SHOWNORMAL);
            cerr<<"Explorer started."<<endl;
        } else {
            cout << "未找到panoid值。" << endl;
        }
    }
    return 0;
}
