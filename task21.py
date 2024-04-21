from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}

com = product(*[data[key] for key in sorted(data.keys())])

for comb in com:
    print(''.join(comb))
