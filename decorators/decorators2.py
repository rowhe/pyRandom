def hello():
    welcome_phrase = "Hello"
    def welcome_print(name: str):
        print(f"{welcome_phrase}, {name}")
        def tmp():
            welcome_phrase + name
    return welcome_phrase

count = 50
def wrapper():
    count =+ 1
    print(count)

wrapper()
