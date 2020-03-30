#1
n = input().lower()
s = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
time = 0
for i in range(len(n)):
    for j in s:
        if n[i] in j:
            time += s.index(j) + 3
print(time)

#2
d = {"ABC":3,"DEF":4,"GHI":5,"JKL":6,"MNO":7,"PQRS":8,"TUV":9,"WXYZ":10}
cnt=0
num =input()
for n in num:
    for j in d.keys():
        if str(n) in j:
            cnt +=d.get(j)
print(cnt)

#3
print(sum(min(ord(c)-64,25)*28//89+3for c in input()))