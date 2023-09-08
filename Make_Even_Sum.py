n=int(input())
s=map(int,input().split())
a=0
for i in s:
    a=a+i;
if a%2==0:
    print("1")
else:
    print("0")