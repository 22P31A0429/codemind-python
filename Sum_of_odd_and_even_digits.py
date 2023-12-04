n=int(input())
arr=list(map(int,input().split()))
s=0
p=0
for i in range(0,len(arr)):
    if i==0:
        s+=arr[i]
    elif i%2==0:
        s+=arr[i]
    else:
        p+=arr[i]
if s-p==0:
    print("YES")
else:
    print("NO")