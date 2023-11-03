r,c=map(int,input().split())#Reading rows and columns
mat=[]
for inner_list in range(r):
    inner_list=list(map(int,input().split()))
    mat.append(inner_list)
s=0
s1=0
for inner_list in mat:
    for every_value in inner_list:
        if every_value%2==0:
            s+=every_value
        else:
            s1+=every_value
print(f"{s} {s1}")