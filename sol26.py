# write a python program to sum all the items in a dictionary
marks = {'physics': 3 , 'math': 4 , 'english': 45 , 'computer program': 12 , 'other': 0}
sum = 0
for i in marks:
    sum = sum + marks[i]
print(sum)    
