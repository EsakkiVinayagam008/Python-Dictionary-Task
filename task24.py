Value = 'w3resource'
num = {}
for char in Value:
    if char in num:
        num[char] = num[char] + 1
    else:
        num[char] = 1

print("Character counts:", num)
