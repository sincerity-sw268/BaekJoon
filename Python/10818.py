import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

max_n = n_list[0]
min_n = n_list[0]
for i in n_list:
    if i > max_n:
        max_n = i
    if i < min_n:
        min_n = i
print(min_n, max_n)


