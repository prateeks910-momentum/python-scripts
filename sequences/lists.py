myList = [1,2,3,4]
print(myList)
print(len(myList))
print(myList[1:])
anotherList = [5,6,7,8]
print(myList + anotherList)
# append item to list
myList.append(10)
print(myList)

# pop item from a list
myList.pop()
print(myList)
pi = myList.pop(1)
print(pi)
print(myList)

# sorting example
newList = ['c','a','b']
numList = [4,2,1]
newList.sort()
numList.sort()
print(newList)
print(numList)
numList.reverse()
print(numList)