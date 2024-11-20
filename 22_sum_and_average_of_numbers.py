m=int(input("Enter m"))
n=int(input("Enter n"))
sum=0
i=m+1
if(m>n):
    print("Invalid")
while(i<n):
    sum=sum+i
    i=i+1
print("sum is",sum)
a=n-m-1
print("average is",sum/a)