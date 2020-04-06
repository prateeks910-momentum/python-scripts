from collections import OrderedDict,defaultdict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for i,v in d.items():
    print(f'{i},{v}')