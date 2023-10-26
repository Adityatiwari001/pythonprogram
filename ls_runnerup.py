ls =[int(i)for i in input().split()]

reg =[]
for i in ls:
    if i not in reg:
        reg.append(i)
out = max(reg)        
reg.remove(out)

out1 = max(reg)
print(out1)
