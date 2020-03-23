import sys

A, B, C = map(int,sys.stdin.readline().split())
min = min(A, B, C)
max = max(A, B, C)
print(A+B+C-min-max)

if A>=B:
    if A>=C:
        if B>=C:
            print(B)
        else:
            print(C)
    else: print(A)
elif B>=C:
    if B>=A:
        if C>=A:
            print(C)
        else:
            print(A)
    else: print(B)






