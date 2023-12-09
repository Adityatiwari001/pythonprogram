tup=(1,3,4,32,1,1,1)
reg = []
for i in tup:
    if tup.count(i)>1:
        if i not in reg:
            reg.append(i)
print(tuple(reg))
