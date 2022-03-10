def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper
   
@doubler
def say_whee():
    print("Whee!")
    
say_whee()
