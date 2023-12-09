marks = {'physics': 3 , 'math': 4 , 'english': 45 , 'computer program': 12 , 'other': None}
sum = 0
for i in marks:
    val = marks[i]
    if type (val) == int:
        sum += val
print('total Marks', sum)   
