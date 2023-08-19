a,b,c,d=map(int,input().split())
if(b+c==a or c+d==a or d+b==a or b==a or c==a or d==a):
    print("YES")
else:
    print("NO")