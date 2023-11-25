#include <iostream>
#include <string>
#include <regex>
#include <cstdlib>
#include <Windows.h>


using namespace std;

string GetClipboardText() {
    string text;

    // �򿪼�����
    if (OpenClipboard(NULL)) {
        // ��ȡ�������е��ı�����
        HANDLE hData = GetClipboardData(CF_TEXT);
        if (hData != NULL) {
            char* pszText = static_cast<char*>(GlobalLock(hData));
            if (pszText != NULL) {
                text = pszText;
                GlobalUnlock(hData);
            }
        }

        // �رռ�����
        CloseClipboard();
    }

    return text;
}

int main() {
    while(1){
        // �յ��س�ʱ�Զ���ȡ����������
        cout << "���س����Զ���ȡ������������ΪԭʼURL��" << endl;
        cin.ignore();  // ���Իس���
        string input = GetClipboardText();

        // ʹ��������ʽ��ȡpanoid��ֵ
        regex panoidRegex("panoid=([^&]+)");
        smatch match;

        if (regex_search(input, match, panoidRegex)) {
            // ��ȡpanoid��ֵ
            string panoid = match[1].str();

            // �����µ�URL
            string newUrl = "https://www.google.com/maps/@?cbll=0,0&cbp=0,0,0,0,0&layer=c&panoid=" + panoid;
            cerr<<"new URL Done."<<endl;
            
            // ʹ��ShellExecute��URL
            ShellExecuteA(NULL, "open", newUrl.c_str(), NULL, NULL, SW_SHOWNORMAL);
            cerr<<"Explorer started."<<endl;
        } else {
            cout << "δ�ҵ�panoidֵ��" << endl;
        }
    }
    return 0;
}
