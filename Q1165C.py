n = int(input()) # will be updated at the end!
s = input()

count = 0
ptr = 0
str_len = n
result = ""
even = False
while ptr < n:
    if not even:
        result += s[ptr]
        even = True
    else:
        if not result[-1:] is s[ptr]:
            result += s[ptr]
            even = False
        else:
            count+=1
    ptr+=1

if len(result)%2!=0:
    result = result[:len(result)-1]
    str_len = len(result)
    count+=1

print("{}".format(count))
print("{}".format(result))
