def calculate(value):
    if (value<=1):
        return 0
    total_nos = value // 7
    mod = value % 7
    if (mod >= 1):
        total_nos +=1
    return total_nos

nos_queries = int(input())
for _ in range(0, nos_queries):
    print("{:d}".format(calculate(int(input()))))
