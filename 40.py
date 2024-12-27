# Write a program to create a list of 5 elements where each
#  element is a multiple of 3. Compute cube of every element
#  and store in same list.( with and without list
# comprehension
li=[]
ki=[]
for i in range(1,6):
    li.append(3*i)
li1=[x*3 for x in range(1,6)]

for i in li:
    ki.append(i**3)

ki1=[x**3 for x in li1]
print(li)
print(li1)
print(ki)
print(ki1)