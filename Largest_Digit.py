def large_digit(n):         
    s=-1                    
    while n>0:                       
        t=n%10
        if t>s:
            s=t
        n//=10
    return s
n=int(input())
result=large_digit(n)
print(result)















