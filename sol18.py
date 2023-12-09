# Write a Python program to create the colon of a tuple.
tu = (7,8,9,4,5,6,1,2,3,[7,8,9,4,5,6])
copy_tu = eval(str(tu))
tu[-1].append(100)
print(f'{tu=}')
print(f'{copy_tu=}')
