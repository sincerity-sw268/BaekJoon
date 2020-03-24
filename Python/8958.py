n = int(input())

for i in range(n):
    num=input()
    cnt=0
    score=0
    for j in range(len(num)):
        if num[j] == 'O':
            cnt +=1
            score +=cnt
        elif num[j] == 'X':
            score +=0
            cnt=0
    print(score)

