myList = [1,2,3,4,5]

for lisItem in myList:
    print(lisItem)

print("----tuples-----")
# looping over a list of tuples
myTup = [(1,2),(3,4),(5,6)]

for a,b in myTup:
    print(b)

print("----dictionary-----")
#looping over dictionaries
myDict = {"id":1, "name":"Prateek"}    
for dicItem in myDict:
    print(dicItem)

#break
myData = [1,2,3,4]
print("----break----")
for data in myData:
    if data == 3:
        break
    print(data)
# continue
myData = [1,2,3,4]
print("----continue----")
for data in myData:
    if data == 3:
        continue
    print(data)
# pass    
myData = [1,2,3,4]
print("----pass----")
for data in myData:
    if data == 3:
        pass
    print(data)