#def apna_fun(st):
     

ls = ['aditya varshney','ansh','om','nikky','aditya tiwari','somani','@deeksha yadav']
print('before sorting',ls)
ls.sort(key = lambda st : sum([ord(i) for i in st]))
print('after sorting',ls)
