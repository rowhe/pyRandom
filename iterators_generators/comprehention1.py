import json

a = [i for i in range(10)]
print(a)

b = { i for i in range(10) }
print(b)

list_ = "asdfasdfnsfm"

c = {i: i.upper() for i in list_}
print(c)

g = [g for g in range(5)]
print(g)

list_e = "adg;asdlkfj"
e = json.dumps(({e: e for e in list_e}), indent=4)
print(e)




