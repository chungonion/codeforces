# *snap*
def snap(a):
    # print(a)
    if sorted(a) == a:
        return len(a)
    else:
        # # print (a[n//2:])
        # print (a[:n//2])
        left = snap(a[len(a)//2:])
        right = snap(a[:len(a)//2])
        if left > right:
            return left
        else:
            return right

n = int(input())
a = [int(n) for n in input().strip().split()]
print("{}".format(snap(a)))
