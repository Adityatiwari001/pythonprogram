# write a function to calculate area and perimeter of rectange.
def area(length,breadth):
    return (length*breadth)
def perimeter (length,breadth):
    return 2*(length+breadth)
length = int(input("enter the length"))
breadth = int(input("enter the breadth"))
area = area(length , breadth)
perimeter = perimeter(length , breadth)
print (f'Area of rectange {area}')
print(f'Perimeter of rectange{perimeter}') 
