n=int(input())
s,p=0,1
while n>0:
    rem=n%10
    n=n//10
    s+=rem
    p*=rem
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")