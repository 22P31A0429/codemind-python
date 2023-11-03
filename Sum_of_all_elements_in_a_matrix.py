r,c=map(int,input().split())#Reading rows and columns
matrix=[]
for i in range(r):
    inner_list=list(map(int,input().split()))
    matrix.append(inner_list)
s=0
for inner_list in matrix:
    for every_value in inner_list:
        s+=every_value
print(s)