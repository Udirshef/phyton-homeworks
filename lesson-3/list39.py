lst = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
nested_lst = [lst[i:i+n] for i in range(0, len(lst), n)]
print(nested_lst)
