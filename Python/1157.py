#1
s = input().lower()
cnt = [0 for i in range(26)]
for i in s:
    cnt[ord(i)-97] += 1
m = max(cnt)
if cnt.count(m) > 1:
    print("?")
else:
    print(chr(cnt.index(m)+65))

#2
s = input().lower()
cnt = {c: s.count(c) for c in set(s)}
m = [k for k in cnt.keys() if cnt[k] == max(cnt.values())]
print(m[0]) if len(m) == 1 else print('?')











