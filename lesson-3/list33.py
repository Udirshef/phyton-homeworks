lst = [1, 2, 3, 2, 4, 2]
element = 2
indices = [i for i, x in enumerate(lst) if x == element]
print(indices)
