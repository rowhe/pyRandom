import itertools

def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += 1
    return None

my_gen_func = count(100, 10)
for _ in range(10):
    print(next(my_gen_func))
