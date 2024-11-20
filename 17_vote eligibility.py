age=int(input("Enter your age"))
if(age>18):
    print("You are eligible to vote")
else:
    print("You need to wait for",18-age)
    if(18-age==1):
        print("Year")
    else:
        print("years")