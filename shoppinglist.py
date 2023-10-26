#shopping list
ls = []
while 1:
    item = input("Enter your item")
    if item =="":
        break

    ls.append(item)
ls.sort()
print(ls)
