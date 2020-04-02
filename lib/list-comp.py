mystring = "Hello"
mylist = [letter for letter in mystring]
print(mylist)

mylist2 = [item for item in range(0,15)]
print(mylist2)

mylist3 = [item*2 for item in range(0,15)]
print(mylist3)

mylist4 = [item for item in range(0,15) if item%2==0]
print(mylist4)