list=[2,3,4,5,6,7,8,9,10]
sublist=[2,3,4]
check_sublist= all(item in list for item in sublist)
if check_sublist:
    print("Yes, list is a subset of another list")
else:
    print("No, list is not a subset of another list")