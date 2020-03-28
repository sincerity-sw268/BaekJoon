s = str(input())
alp_list = [-1 for _ in range(26)]

for i in s:
    a = ord(i) - 97
    if (alp_list[a] == -1):
        alp_list[a] = s.index(i)

for i in alp_list:
    print(i,end=" ")

