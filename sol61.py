def prime_or_not(n):
    
        count = 0
        for i in range(1,n+1):
            if n%i == 0:
                count += 1
        if count == 2:
            return "true"
        else:
            return "false"
        
    

lst = [7,8,9,4,5,6,1,2,3,0]
print('before mapping',lst)
out = list(map(prime_or_not,lst))
print('after mapping',out)
