n = input().lower()
s = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
time = 0
for i in range(len(n)):
    for j in s:
        if n[i] in j:
            time += s.index(j) + 3

print(time)