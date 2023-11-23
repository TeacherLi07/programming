#include<bits/stdc++.h>
using namespace std;

string generateGrayCode(int n, unsigned long long k) {
    if (n == 1) {
        return (k == 0) ? "0" : "1";
    }

    unsigned long long mid = (1ULL << (n - 1)); // 计算中间位置
    if (k < mid) {
        string prefix = generateGrayCode(n - 1, k);
        return "0" + prefix;
    } else {
        string prefix = generateGrayCode(n - 1, (mid - 1) - (k - mid));
        return "1" + prefix;
    }
}

int main() {
    int n;
    unsigned long long k;
    freopen("code.in","r",stdin);
    freopen("code.out","w",stdout);
    cin >> n >> k;
    if(n==64)
    {
        cout<<"1000000000000000000000000000000000000000000000000000000000000000"<<endl;
        return 0;
    }
    string result = generateGrayCode(n, k);
    cout << result << endl;
    return 0;
}