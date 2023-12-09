# write a function to check number is prime or not.
def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        return "number is prime"
    else:
        return "number is not prime"
num =2
out = prime(num)
print(out)
