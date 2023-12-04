def perfect_square(n):
    k=int(n**0.5)
    return n==(k*k)
n=int(input())
arr=list(map(int,input().split()))
arr=set(arr)
s=0
for i in arr:
    if perfect_square(i):
        s+=i
print(s)