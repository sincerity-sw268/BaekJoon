import sys

n = int(sys.stdin.readline())

even = n//2
odd = n-n//2

for i in range(n):
    print("* " * odd)
    print(" *" * even)
