from collections import namedtuple

Dog = namedtuple('Dog','age breed name')

d = Dog(age=5,breed='doberman',name='doby')

print(d)