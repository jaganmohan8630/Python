name="Jagan Mohan"
age=18
print("My name is %s, I am %d years old"%(name,age))
print("My name is {}, I am {} years old".format(name,age))
print(f"My name is {name}, I am {age} years old")
from string import Template
t=Template("My name is $name, I am $age years old").substitute(name="Jagan Mohan",age=18)