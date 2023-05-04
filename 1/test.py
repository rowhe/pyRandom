# import itertools
#
# def first_gen(input_: int):
#     yield input_
#     input_ += 1
#     print(input_)
#
# my_first_gen = first_gen(5)
#
# print(next(my_first_gen))
#
# print(next(my_first_gen))
#
# def second_gen(input_):
#     yield input_
#     input_ += 1
#
#     yield input_
#     input_ += 1
#
#     return input_
#
# my_second_gen = second_gen(10)
#
# print(next(my_second_gen))
# print(next(my_second_gen))
# print(next(my_second_gen))

# def my_animal_generator():
#     yield 'korova'
#     print('---')
#     for animal in ['kot', 'sobaka', 'medved']:
#         yield animal
#     print('---')
#     yield 'kit'
#
# a = my_animal_generator()
# print(next(a))
#
# print(next(a))
# for i in a:
#     print(i)
#
# for i in my_animal_generator():
#     print(i)

def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


fib_gen = fib()
for num in fib_gen:
    print(num)
    if num > 10000:
        break

print(next(fib_gen))

fib_gen = fib()
fib_gen.close()

for i in fib_gen:
    print(i)

fib_gen
next(fib_gen)