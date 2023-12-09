# Write a python program to remove the empty tuples from a given list of tuples.

lst = [(),(),('',), (),(34,2,4),([],), ()]

for i in range(lst.count(())):
        lst.remove(())
        
print(lst)
