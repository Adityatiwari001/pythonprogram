# scope of variable.
def add():
    # local scope
    a = 0
# global scope    
a = 52
add()
print(a)
# we can't access/use local variable in a global variable,but global variable use/access in local variable.
