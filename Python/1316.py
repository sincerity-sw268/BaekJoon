#!
n = int(input())

for i in range(n):
    word = input()
    for i in range(1,len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            n -=1
print(n)

#2
n = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        n+=1
print(n)
