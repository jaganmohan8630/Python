# Create iterables 3 (list, tuple, string) with redundant data.
#  Convert them to set and print
li=[1,4,3]
ki=(3,4,1)
str="jagan"
m=[li,ki,str]
for i in m:
    print(set(i))
