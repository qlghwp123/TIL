n = int(input()) % 12

if n < 3:
    print("winter")
elif n >= 3 and n < 6:
    print("spring") 
elif n >= 6 and n < 9:
    print("summer") 
else:
    print("fall")
