N = int(input())
check = N
count = 0
while True:
    temp = N // 10 + N % 10
    new_N = (N % 10)*10 + (temp % 10)
    count += 1
    N = new_N
    if new_N == check:
        break
print(count)