def func():
    print("function in one.py")

print("Top level function one.py")

if __name__=="__main__":
    print("one.py was run directly")
else:
    print("one.py was imported")    
