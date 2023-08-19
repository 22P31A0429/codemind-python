a,b,c,d=map(int,input().split())
r=a-b
p=b*c
if(c>=d):
    p=p+r*d
else:
    p=p+r*c
print(p)