# Write a program to read 10 values from user into a list.
#  Create a new list which retains the positive values as they
#  are and replaces all negative values with 0

a=[]
b=[]
for i in range(10):
    tatish=int(input("enter a"))
    a.append(tatish)
print(a)
for i in range(len(a)):
    if a[i]<0:
        a[i]=0
    b.append(a[i])
print(b)