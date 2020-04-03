#1
a,b,v=map(int,input().split())
d = 0
if (v-b) % (a-b) !=0:
    d = ((v-b) // (a-b))+1
else:
    d = (v-b) // (a-b)
print(d)

#2
a,b,v=map(int,input().split())
d = ((v-b) / (a-b))
print(int(d) if d == int(d) else int(d) +1)