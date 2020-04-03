for _ in range(int(input())):
    h, w, n = map(int,input().split())
    a = n % h; b = n//h +1
    if a == 0: b -=1; a=h
    print(a*100+b)
