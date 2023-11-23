m=int(input())
n=int(input())
i=0
if n>m:
    m,n=n,m
while m%n!=0:
    m,n =n,m%n
    i+=1
print(n,"count",i)
