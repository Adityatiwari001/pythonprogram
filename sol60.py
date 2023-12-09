lst = [7,8,9,4,5,6,1,2,3,0]
print('before mapping',lst)
out = list(filter(lambda n : n%2==1,lst)) #filterring
print('after mapping',out)
