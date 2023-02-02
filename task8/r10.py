from itertools import permutations

s = set()
for word in permutations('kapkan'):
    word = ''.join(word)
    if 'kk' not in word and 'aa' not in word:
        s.add(word)
print(len(s))
#