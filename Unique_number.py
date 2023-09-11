def unique_number(num):
    num_str=str(num)
    return len(num_str)==len(set(num_str))
num=int(input())
if unique_number(num):
    print("Unique Number")
else:
    print("Not Unique Number")