#include<bits/stdc++.h>
using namespace std;
int main()
{
    char jj[4]={'A','T','C','G'};
    string ejz,xulie="";
    int tmp,flag=0;
    getline(cin,ejz);
    for(int i=0;i<ejz.length();i+=2)
    {
        if(ejz[i]==' ')
        {
            xulie[flag++]=' ';
            continue;
        }
        tmp=ejz[i]*10+ejz[i+1];
        switch (tmp)
        {
            case 0:
                xulie[flag++]=jj[0];        
            case 1:
                xulie[flag++]=jj[1];
            case 10:
                xulie[flag++]=jj[2];
            case 11:
                xulie[flag++]=jj[3];
        }
    }
    cout<<xulie<<endl;
    system("pause");
    return 0;
}