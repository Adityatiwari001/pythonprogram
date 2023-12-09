def add():
    def fun1():
        abc = 12
    def fun2():
        nonlocal abc
        abc = 24
    def fun3():
        global abc
        abc = 56
    
    abc = 10
    fun1()
    print(abc)
    fun2()
    print(abc)
    fun3()
    print(abc)
    

#global scope
abc = 100
add()
print(abc)
