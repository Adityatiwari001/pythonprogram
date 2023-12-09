# write a function to calculate area and circumfrance of a circle.
def area(r):
    return (3.14*r*r)
def circum (r):
    return 2*(3.14*r)
r = int(input("enter the radius"))

area = area(r)
circumfrance = circum(r)
print (f'area of circlr {area}')
print(f'circumfrance of circle{circumfrance}')  
