n=int(input())
a=0
b=1
if(n==0):
    print("0")
c=a+b
while(c<=n):
    a=b
    b=c
    c=a+b
if((n-b)==(c-n)):
    print("%d %d"%(b,c))
elif((n-b)<=(c-n)):
    print(b)
else:
    print(c)