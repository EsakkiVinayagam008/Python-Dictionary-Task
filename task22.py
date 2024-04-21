import heapq
dic = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

values = heapq.nlargest(3, dic.values())

print("Highest 3 values in the dictionary:")
for value in values:
    key = next(key for key, val in dic.items() if val == value)
    print(f"{key}: {value}")
