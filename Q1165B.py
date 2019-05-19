n= int(input())
a = [int(n) for n in input().strip().split()]
a.sort()

days = 0
queue_head = 0
queue_tail = n
for k in range(1,n+1):
    while queue_head < queue_tail and k > int(a[queue_head]):
        queue_head += 1
    if queue_head < queue_tail and k <= int(a[queue_head]):
        days+=1
        queue_head += 1
print("{}".format(days))
