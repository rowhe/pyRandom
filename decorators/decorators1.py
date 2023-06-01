# def twice_func(inside_func):
#     inside_func()
#     inside_func()
#
# def hello():
#     print("Hello")
#
# test = twice_func(hello)
#
# test()

def hello():
    welcome_phrase = "Hello"
    def welcome_print(name: str):
        local_var = "local var"
        print(f"{welcome_phrase}, {name}")
    return welcome_print

inside_func = hello()
print(inside_func)

inside_func(name="world")
inside_func(name="test")

