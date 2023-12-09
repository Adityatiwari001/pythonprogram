# file handling : reading and writing operations with local file.
'''
1. open the file.
2. do the operation (read/write).
3. close the file 

# file open 
file_object = open('file_name(with path)','filemode')
'''
f = open('sample.txt','w')
print('hello world',file = f)
f.close()
