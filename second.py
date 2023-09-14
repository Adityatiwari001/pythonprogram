sec = int(input("Enter the time in sec"))
hr  = sec//3600
sec = sec%3600
min = sec//60
sec = sec%60
print(f" time: {hr}:{min}:{sec}")
