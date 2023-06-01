mylist = list(range(10))

x = [i**3 for i in mylist if i > 4 and i % 2 == 1]
y = {f"{x} * {y}": x * y for x in range(10) for y in range(7, 0, -1) if x * y > 10}

print(x)
print(y)

# a = [ i for i in range(7,0,-1)]
# print(a)