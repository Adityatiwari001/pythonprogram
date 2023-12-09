def add():
    # local scope
    global abc
    print(abc)
    abc = 0
# global scope    
abc = 52
add()
print(abc)
