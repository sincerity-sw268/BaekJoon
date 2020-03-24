n = int(input())
score = list(map(int,input().split()))
m=max(score)
avg=0
for i in range(n):
    score[i] = score[i]/m*100
    avg += score[i]

print("%.2f" %(avg/n))
