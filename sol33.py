# main code
a = int(input('Enter the number'))
count = 0
for i in range(1,a+1):
    if a % i == 0:
        count += 1
print(count == 2)
