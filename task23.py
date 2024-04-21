from collections import Counter

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

values = Counter()
for d in data:
    values[d['item']] += d['amount']
print("Combined values:", values)
