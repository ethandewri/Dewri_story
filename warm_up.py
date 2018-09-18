"""
write a program that will ask the user for a num,ber (Intergers only)
and return a statement tha he number is EVEN or ODD

% = modulus
  = returns the remainder only
"""
x=float(input("PLease enter a number:"))

if (x%2==0):
    print('the number '+ str(x) + 'is even!')
    
    
    else: 
      print('the number) '+ str(x) + 'is odd!')