a = int(input("please enter side a: "))
b = int(input("please enter side b: "))
c = int(input("please enter side c: "))

#A.
if (a + b <c):
    print ("this is not a triangle")

#B.
if (a**2 + b**2 ==c**2):
    print("this is a right triangle")

#C.
if (a**2 + b**2 <c**2):
    print("this is an obtuse triangle")

#D.    
if (a**2 + b**2 >c**2):
    print('this is an acute triangle')
    
else: 
    print ("this is not a right triangle")
    