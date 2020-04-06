from collections import Counter

l = [1,2,2,3,3,3,4,4,4,4]

c = Counter(l)

print(c.items())
print(c.most_common(2))
print(dict(c))
