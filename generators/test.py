def gen_cube(n):
    for x in range(n):
        yield x ** 3

for val in gen_cube(5):
    print(val)