
n = int(input())

for i in range(n):
    num, s = input().split()
    text = ""
    for j in s:
        text += int(num) * j
    print(text)

    exec("r,_,*s=input();print(''.join(i*int(r)for i in s));" * int(input()))
