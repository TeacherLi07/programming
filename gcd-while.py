m=int(input())
n=int(input())
i=min(n,m)
while 1:
    if m%i==0 and n%i==0:
        break
    i=i-1
print(i)