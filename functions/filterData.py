def checkEven(num):
    return num%2 == 0

mynums = [1,2,3,4,5]

print(list(filter(checkEven, mynums)))