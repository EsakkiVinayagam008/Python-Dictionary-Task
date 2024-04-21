data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
value=set()
for i in data:
    for j in i.values():
        value.add(j)
print("Unique Value :",value)