#include<bits/stdc++.h>
using namespace std;
const int N=110000;
int n,add[N],thick[N],maxthick;
int main(){
    freopen("396.txt","r",stdin);
    n=31148;
	for(int i=0;i<n;i++){
		int s,t,during;
		cin>>s>>t>>during;
        if(during>600){
            add[s]++;
            add[t+1]--;
        }
	}
	thick[0]=add[0];
	maxthick=thick[0];
	for(int i=1;i<=n;i++){
		thick[i]=thick[i-1]+add[i];
		maxthick=max(thick[i],maxthick);
	}
	cout<<maxthick<<endl;
	return 0;
}
