import sys

n = int(sys.stdin.readline())

for i in range(1, n*2):
    if i <= n:
        print("*"*i)
    else:
        print("*"*(2*n-i))

