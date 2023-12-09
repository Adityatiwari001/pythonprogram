# example of global variable use/access in local variable.
def add():
    # local scope
    print(abc)
    
# global scope    
abc = 52
add()
print(abc)
