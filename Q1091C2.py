import operator
num = int(input())
fun_list = {1: 1}
num_sum = 1 + num

for k in range(2, num):
    if num % k == 0:
        fun_sum = sum(list(range(1, num+1, k)))
        fun_list[fun_sum] = fun_sum
    num_sum +=k
sorted_fun = sorted(fun_list.items(), key=operator.itemgetter(1))
for i in (sorted_fun):
    print(str(i[0]), end=" ")
print(str(num_sum))
