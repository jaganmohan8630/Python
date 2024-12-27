# Write a program to create a tuple (name, age, city, college),
#  Get all values from user . Then read number of years from
#  user, calculate the age of the person after those n years
#  and put it back to a tuple.

a=input("Enter your name")
b=int(input("Enter your age"))

li=[a,b]
print(tuple(li))
c=int(input("Enter your age"))
li[1]+=c
print(tuple(li))
