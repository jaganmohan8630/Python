salary=int(input("Enter your salary"))
typ=input("Enter NT or T")
print("Actual salary is",salary)
if(typ=="NT"):
    print("Bonus salary is",(5/100)*salary)    
    print("Total salary is",(5/100)*salary + salary)
if(typ=="T"):
    print("Bonus salary is",(10/100)*salary)
    print("Total salary is",(10/100)*salary + salary)