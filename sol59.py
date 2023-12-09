lst = [7,8,9,4,5,6,1,2,3,0]
print('before mapping',lst)
out = list(map(lambda n : n%2==0,lst)) #mapping
print('after mapping',out)
