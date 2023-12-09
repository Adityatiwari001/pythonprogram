# write a function to find factorial of a number but also store the factorial calculated in a dic as done in the fibinnci series.
def factorial(num):
    fac = 1
    for i in range(1,num+1):
        fac*= i
    return fac
dct = {}
while 1:
    num = 5
    out = factorial(num)
    print(f'factorial is given number{num} if {out}')
    dct[num] = out
    print("do you want continue y/n")
    if input() != "y":
        print(f'your all result {dct}')
        break
