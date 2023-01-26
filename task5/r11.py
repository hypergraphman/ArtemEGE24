def f(n):
    s1 = f'{n:b}'
    s2 = s1[1:]
    s3 = int(s2, 2)
    return n - s3


print(f(11))
s = set()
for i in range(500, 5000 + 1):
    s.add(f(i))
print(s)
print(len(s))