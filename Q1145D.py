n = int(input())
a = [int(n) for n in input().strip().split()]
print((min(a)^a[2])+2)
