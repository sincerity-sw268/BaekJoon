n =int(input())
a = list(map(int,input().split()))
res_cnt = 0
for i in a:
    cnt = 0
    if i==1:
        continue
    for j in range(2,i+1):
        if(i%j == 0):
            cnt +=1
    if cnt ==1 :
        res_cnt +=1
print(res_cnt)