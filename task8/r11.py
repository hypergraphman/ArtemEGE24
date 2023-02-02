from itertools import product

c = 0
for word in product('SKOLA', repeat=3):
    word = ''.join(word)
    if word.count('K') == 1:
        c += 1
print(c)
#