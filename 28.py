#  Write a for loop to generate the sequence 1 1 3 6 10 15 21 
# ….. upto n integers
n=int(input("emter your number:"))
a=[1]
sum=0
for i in range(1,n):
    sum+=i
    a.append(sum)
print(a)
# n=int(input("Enter n"))
# sum=0
# for i in range(1,n):
#     print(sum)
#     sum=sum+i
