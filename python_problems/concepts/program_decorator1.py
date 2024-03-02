# Nested Function

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
#
#
# add_five = outer(5)
# result = add_five(6)
# print(result)


# def add(x, y):
#     return x + y
#
#
# def calculate(func, x, y):
#     return func(x, y)
#
#
# result = calculate(add, 10, 20)
# print(result)


# def greeting(name):
#     def hello():
#         return "Hello, " + name + "!"
#     return hello
#
#
# greet = greeting("Atlantis")
# print(greet())


# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#
#         func()
#     return inner
#
#
# # define ordinary function
# def ordinary():
#     print("I am ordinary")
#
#
# decorated_func = make_pretty(ordinary)
#
#
# decorated_func()


# def make_pretty(func):
#
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
#
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#
#
# ordinary()


# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Zero division not allowed!")
#             return
#         return func(a, b)
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
#
# divide(2, 5)
# divide(2, 0)


def start(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@start
@percent
def printer(msg):
    print(msg)


printer("Hello")

