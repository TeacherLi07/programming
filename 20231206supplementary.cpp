#include <bits/stdc++.h>
using namespace std;
int f[100][100]; // -50 = 0, 0 = 50

int f_calc(int i, int j)
{
    if( f[i][j] != -1 )   return f[i][j];
    else f[i][j] = f_calc(i-1,j-2) + f_calc(i-1,j-1) + f_calc(i-1,j+1);
    return f[i][j];
}
int main()
{
    memset(f, -1, sizeof(f));
    // set the whole row of f[1] to 0
    for (int i=0; i<100; i++)
        f[1][i]=0;
    f[1][49]=1;
    f[1][51]=1;
    f[1][52]=1;
    cout<<f_calc(15,27+50)<<endl;
    system("pause");
    return 0;
}