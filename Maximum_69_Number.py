n=input()
list=[i for i in n]
for i in range(0,(len(list))):
    if(list[i])=='6':
        list[i]='9'
        break
for i in list:
    print(i,end=" ")