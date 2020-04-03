x = int(input())

i = 1
cnt = 1
while x>i:
    x -= i
    i +=1
    cnt+=1

if cnt % 2 != 0:
    up = (cnt+1-x)
    down = x
else:
    up = x
    down = (cnt + 1 - x)

print("{}/{}".format(up,down))



