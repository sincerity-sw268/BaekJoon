n_num=set(range(1,10001))
g_num=set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    g_num.add(i)
s_num=n_num-g_num

for i in sorted(s_num):
    print(i)




