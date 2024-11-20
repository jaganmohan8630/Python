oparation=input("Enter the operation +,-,*,/,% \n")
a=int(input("Enter a"))
b=int(input("Enter b"))
if oparation=='+':
    print("sum of a and b is",a+b)
elif oparation=='-':
    print("subtraction of b and from a is",a-b)
elif oparation=='*':
    print("multiplication of a and b is",a*b)
elif oparation=='/':
    print("division of a and b is",a/b)
elif oparation=='%':
    print("a modulus b is",a%b)
else:
    print("Enter a valid operator")