'''
    A basic function testing try/catch/finally
'''
def ask_for_init():
    '''
        This function is asking for user input till he doesn't
        provides a number that can be converted into integer
    '''
    while True:
        try:
            num = int(input("Please enter a number: "))
        except ValueError:
            print("Whoops! that cannot be converted into an integer")
            continue
        else:
            print("Yes, thats correct")
            print(num)
            break
        finally:
            print("End of try/catch/finally")

ask_for_init()
