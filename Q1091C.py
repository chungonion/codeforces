import operator
num = int(input())

fun_list = {}
for k in range (1,num+1):
    fun = {1:1}
    current = 1
    current += k
    # print ("{:d}".format(fun[1]))
    current -=1
    current %= num
    current +=1

    if current not in fun:
        fun[current] = current

    while (current != 1):
        current += k-1
        current %= num
        current += 1
        if current not in fun:
            fun[current] = current
            # print(str(current))

    # print("{:d}".format(sum(fun.values())))
    fun_list[sum(fun.values())] = sum(fun.values())

sorted_fun = sorted(fun_list.items(), key=operator.itemgetter(1))
# print(sorted_fun)

for i in (sorted_fun):
    print ("{:d}".format(i[0]),end=" ")
print()


        

