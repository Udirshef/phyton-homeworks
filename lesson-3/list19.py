list=[23,4,12,4,5,6,7,8,9,10]
old=23
new='qwerty'
if old in list:
    list[list.index(old)]=new
print(list)