alphabet ="abcdefghijklmnopqrstuvwxyz"
s = str(input().upper())
alp_list = [0 for _ in range(26)]


for i in s:
    a = ord(i) - 65
    alp_list[a] += 1
num = max(alp_list)

if alp_list.count(num) >=2:
    print("?")
else:
    print(chr(alp_list.index(num)+65))









