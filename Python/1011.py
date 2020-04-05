import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    diff = y-x
    if diff <=3:
        print(diff)
    else:
        d = int(math.sqrt(diff))
        if diff ==d **2:
            print(d*2-1)
        elif d**2<diff<=d**2+d:
            print(d*2)
        else:
            print(d*2+1)
