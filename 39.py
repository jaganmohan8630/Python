# Write a program to create a list of 8 elements where each
#  element is a multiple of 5. Raise every element to the
#  power of same element and store in a new list.(with and
#  without list comprehension
li=[]
ki=[]
for i in range(1,9):
    li.append(5*i)
li1=[x*5 for x in range(1,9)]

for i in li:
    ki.append(i**i)

ki1=[x**x for x in li1]
print(li)
print(li1)
print(ki)
print(ki1)