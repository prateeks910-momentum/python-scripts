# args example
def myfunc1(*args):
    return sum(args)

print(f'The sum of arguments is {myfunc1(2,3,4,5,6)}')

def myfunc2(**kwargs):
    print(f'My favourite fruit is {kwargs["fruit"]}')

myfunc2(fruit="mango")