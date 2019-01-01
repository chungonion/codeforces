y, b, r = list(map(int, input().split()))

max = 0
if (y+1 <= b) and (y+2 <= r) and (y+y+1+y+2) > max:
    max = y+y+1+y+2


if (b-1 <= y) and (b+1 <= r) and (b-1+b+b+1) > max:
    max = b-1+b+b+1

if (r-2 <= y) and (r-1 <= b) and (r-2+r-1+r) > max:
    max = r-2+r-1+r

print("{:d}".format(max))
