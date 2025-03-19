list=[12,34,56,34,56,7]
if len(list)%2==0:
    print(list[int(len(list)/2+1)],list[int(len(list)/2)])
else:
    print(list[int(len(list)/2)])