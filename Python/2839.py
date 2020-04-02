n = int(input())

five = n//5
n = n%5

while n>=0:
    if n%3==0:
        three= n//3
        n = n%3
        break
    five -=1
    n += 5
if five<0 or three <0:
    print("-1")
else: print(five+three)