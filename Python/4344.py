n = int(input())

for i in range(n):
    cnt = 0
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]

    for j in num[1:]:
        if j > avg:
            cnt +=1
    print("%0.3f%%"%round(cnt/num[0]*100,3))

