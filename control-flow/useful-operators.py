# range operator

print('--------- range operator -------')

for i in range(10):
    print(i)

for j in range(1,10):
    print(j)

for k in range(1,10,2):
    print(k)

# enumerate operator

print('----- enumerate operator ---------')

name='abcde'

for index,val in enumerate(name):
    print(f'letter at {index} is {val}')

# zip operator

print('------ zip operator ----------')

myList1 = [1,2,3,4,5]
myList2 = ['a','b','c','d','e']

for item in zip(myList1,myList2):
    print(item)

# list opeartor

print('----- list operator ------')
print(list(zip(myList1,myList2)))

# in operator

print('---- in operator -------')
print(1 in [1,2,3,4,5,6])
print(1 in (1,2))
print(1 in [(2,4),(1,3)])
print("id" in {"id":1, "name":"prateek"})

# min/max operator
print('---- min/max operator -------')
print(max(myList1))
print(min(myList1))


