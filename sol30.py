# write a python program to map two lists into a dictionary
keys = ['name','totalmarks']
values = ['anoop', 34]

dct = {}
for i in range (len(keys)):
    dct[keys[i]] = values[i]
print(dct)
