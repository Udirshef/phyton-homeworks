lst = [1, 2, 2, 3, 3, 4, 4]
unique_lst = []
[unique_lst.append(x) for x in lst if x not in unique_lst]
print(unique_lst)
