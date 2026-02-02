


# def dFun(fn):
#    print("wow")
#    def df(*a,**b):
#         print("Welcome")
#         print(a,b)
#         fn()
#         print("Thanks")
        
#    return df

# @dFun
# def hello():
#     print("Hello, World!")


# hello(12,name="IUK")
# # dFun(hello)(12,45,name ="hello",hel= "how")




def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Calling {original_function.__name__} with args={args}, kwargs={kwargs}")
        result = original_function(*args, **kwargs)
        print(f"{original_function.__name__} finished executing.")
        return result
    return wrapper_function

@decorator_function
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet("Ijaz", 21)