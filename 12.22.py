ys=[]
a=0
ans=0
i=0
k=0
while a!=-1:
    a=float(input())
    ys.append(a)
    ans+=a
    i+=1
ys.remove(-1)
i-=1
print(ys,ans,ans/i)
while k<i:
    if ys[k]>ans/i:
        print(ys[k])
    k+=1
# for i in range(1,5,1):
#     if i==3:
#         break;
#     print(i);