#inpiut section
principal=int(input("enter the principal"))
rate=int(input("enter the rate"))
time=int(input("enter the time"))
#logic section
si=(principal*rate*time)/100
amount=(principal+si)
#display section
print("the simple interest is",si)
print("tne amount is",amount)
