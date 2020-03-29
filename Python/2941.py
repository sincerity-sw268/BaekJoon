
word = input()
al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in al:
    word = word.replace(a,'A')
print(len(word))