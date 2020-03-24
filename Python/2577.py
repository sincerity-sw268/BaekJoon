
a = int(input())
b = int(input())
c = int(input())

s = str(int(a*b*c))

for i in range(0,10):
    print(s.count(str(i)))