my_list = [1, (43, 26), "test", ["end"]]

my_list_iter = iter(my_list)

while True:
    try:
        print(next(my_list_iter))
    except StopIteration:
        break
print("\nIterator ended")