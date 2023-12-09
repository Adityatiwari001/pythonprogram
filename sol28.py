# write a python program to multiply all the items in a dictionary

marks = {'physics': 3 , 'math': 4 , 'english': 45 , 'computer program': 12 , 'other': None}
sum = 1
for i in marks:
    val = marks[i]
    if type (val) == int:
        sum *= val
print('total Marks', sum)  
