n,x,y = [int(n) for n in input().strip().split()] # n = no. of digits, y<x<n
# print("{} {} {}".format(n,x,y))
num = input()

value = 0
for i in range(0,x):
    if i == y:
        if not num[n-i-1] is '1':
            value+=1
    else:
        if not num[n-i-1] is '0':
            value+=1
print("{}".format(value))
