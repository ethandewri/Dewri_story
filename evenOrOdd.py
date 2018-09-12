"""
Write a program that will take a number (Integers Only) and return
a statement tha will let the user know if it is even or odd
"""
print ("Is the number even or odd?")

x = int(input("please enter a number: "))

if (x%2==0):
    print ("Even")

elif (x%2==1):
    print ("Odd")
    