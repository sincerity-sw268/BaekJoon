s = input()
word=[-1 for i in range(26)]

for i in s:
    word[ord(i)-97]=s.index(i)

for i in range(len(word)):
    print(word[i],end=' ')

