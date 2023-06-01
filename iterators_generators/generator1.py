# import itertools
#
# a = (i**2 for i in itertools.count(1,1))
#
# for i in range(10):
#     print(next(a))
#
# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
#     return None
#
# my_gen_func = count(100, 10)
# for _ in range(10):
#     print(next(my_gen_func))

# def count2(start = 500, step = 50):
#     counter = start
#     while True:
#         counter += step
#         yield counter
#     return None
#
# some_gen = count2(70, 2)
#
# for i in range(10):
#     print(next(some_gen))
#
# def first_gen(input_: int):
#     yield input_
#     input_ += 1
#     print(input_)
#     #return None
#
#
# my_first_gen = first_gen(5)
# print(next(my_first_gen))
# print(next(my_first_gen))

# def second_gen(input_):
#     yield input_
#     input_ += 1
#
#     yield input_
#     input += 1
#
#     return input_
#
# my_second_gen = second_gen(10)
#
# print(next(my_second_gen))
# print(next(my_second_gen))
# print(next(my_second_gen))

def my_animal_generator():
    # yield 'корова'
    # print('---')
    for animal in ['кот', 'собака', 'медведь']:
        yield animal
    # print('---')
    # yield 'кит'

a = my_animal_generator()
print(next(a))


for i in my_animal_generator():
    print(i)
