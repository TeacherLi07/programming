from datetime import datetime
def is_prime4(x):
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True

a=0
n=0
while True:
    a=a*10+1
    n+=1
    print(n,"\tstart at ",datetime.now(),sep="",end="")
    if n%3==0 or (not is_prime4(n)):
        print("\tcontinue",sep="")
        continue
    else:
        print()
    if is_prime4(a):
        print("find!",n,a,sep="\t")
    