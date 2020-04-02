myFile = open('text.txt')
print(myFile.read())
print(myFile.read())
myFile.seek(0)
print(myFile.read())
myFile.seek(0)
print(myFile.readlines())
myFile.seek(0)
print(myFile.readline())
myFile.close()

print("----------")
# avoid manual close
with open('text.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)
