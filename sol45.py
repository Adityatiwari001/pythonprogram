# arbitrary positional 
def optional_sum_mul(*obj,op):
    if op=='Add':
        s = 0
        for i in obj:
            s+=i
        return s
    elif op == 'mul':
        s = 1
        for i in obj:
            s*=i
        return s
        


     

out = optional_sum_mul(5,6,51,53,865,55,41, op='mul')
print(out)
