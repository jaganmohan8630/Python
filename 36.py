# Write a program to create a list and perform the following
#  operations: +, *, Slicing , del

jj=[1,2,3,4]
s=sum(jj)
print(s)
mul=1
for i in jj:
    mul=mul*i
print(mul)
li=jj[1:3]
print(li)
del jj[2]
print(jj)