# write a python program to get the maximum and minimum value in a dictionary
marks = { 'math': 34 , 'physics' : 56 , 'english ': 88 }
val = 0
key = ''

for i in marks:
    m = marks[i]
    if val < m:
        val = m
        key = i
print( 'maximum:', key,val) 
val1 = 0
key1 = ''

for i in marks:
    m = marks[i]
    if val > m:
        val = m
        key = i
print( 'minimum:', key,val) 
