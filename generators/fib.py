def fib(n):
    n1=0
    n2=1
    for x in range(0,n):
        if x <= 1:
            yield x
        else:
            res = n2+n1
            n1 = n2
            n2 = res
            yield res


for val in fib(10):
    print(val)        