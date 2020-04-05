#1
def sum(k,n):
    if k == 0:
        return n
    s= 0
    for i in range(1,n+1):
        s += sum(k-1,i)
    return s

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(sum(k,n))

    print(sum)

#2
for _ in range(int(input())):
    k=int(input()); n=int(input())
    v = [i for i in range(1,n+1)]
    for _ in range (k):
        for j in range(1,n):
            v[j] +=v[j-1]
    print(v[-1])
