def new_decorator(func):
    def wrapper():
        print("I run before the function is executed")
        func()
        print("I run after the function is executed")
    return wrapper

@new_decorator
def func_that_needs_decoration():
    print("I need decoration")    


func_that_needs_decoration()
