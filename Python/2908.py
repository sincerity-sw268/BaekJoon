#1
a,b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a>b:
    print(a)
else:
    print(b)

#2
print(max(input()[::-1].split()))