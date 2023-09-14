n1 = eval(input("Enter the first side"))
n2 = eval(input("Enter the second side"))
n3 = eval(input("Enter the third side"))

s = (n1+n2+n3)//2

area = (s*(s-n1)*(s-n2)*(s-n3))**0.5

print("areaa",area)
