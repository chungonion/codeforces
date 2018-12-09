from sys import argv
import math


def check(m, n, a):
    h_need = math.ceil(int(m) / int(a))
    w_need = math.ceil(int(n) / int(a))
    total = h_need * w_need
    print(str(total))
    return 0

temp = input()
temp = temp.split()
check(temp[0],temp[1],temp[2])
