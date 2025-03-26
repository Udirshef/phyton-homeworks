list1 = [1, 1, 2]
list2 = [2, 3, 4]

result = []


for element in list1:
    if element not in list2:
        result.append(element)
    elif list1.count(element) > list2.count(element):
        result.extend([element] * (list1.count(element) - list2.count(element)))

for element in list2:
    if element not in list1:
        result.append(element)
    elif list2.count(element) > list1.count(element):
        result.extend([element] * (list2.count(element) - list1.count(element)))

# Print the result
print(result)




