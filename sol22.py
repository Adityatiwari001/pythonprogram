# map 
lst = [23,45,6,7]
new_list = []
for i in lst :
    #new_list.append (float(i))
    #new_list = map(float,lst)
    new_list = list(map(float,lst))
print(new_list)
