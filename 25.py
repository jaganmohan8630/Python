positive=0
negative=0
zero=0
while True:
     n=int(input("Enter n and -1 to stop"))
     if(n==-1):
         break
        #  print("You are done")
     elif(n>0):
         positive+=1
     elif(n<0):
         negative=negative+1
     else:
         zero=zero+1
print("Number of positive's are",positive)
print("Number of negative's are",negative)
print("Number of zero's are",zero)
