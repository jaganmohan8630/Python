def prime(n):
    if(n<=1):
            return False
    if(n==2):
            return True
    for i in range(2,n):
        if(i%n==0):
            return False
    return True
n=int(input("Enter n"))
if(prime(n)):
   print("It is a prime number")
else:
   print("It is not a prime number")