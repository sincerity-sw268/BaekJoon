#1
n = int(input())

if n ==1:
    cnt = 1
else:
    i = 1
    cnt = 1
    while n>=2:
        n -= i*6
        cnt += 1
        i += 1
print(cnt)

#2
print(int((int(input())/3-.1)**.5+1.5))
