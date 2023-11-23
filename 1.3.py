s=input()
ans=0
for i in range(0,len(s)):
    if '0'<=s[i]<='9':
        print(s[i],end="")
        ans+=int(s[i])
print("\n",ans,sep="")