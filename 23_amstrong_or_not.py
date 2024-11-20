n=int(input("Enter n"))
t=n
sum=0
n=t
while(n>0):
    d=n%10
    sum=sum+d**3
    n=n//10

if(sum==t):
     print("Armstrong")
else:
     print("Not")