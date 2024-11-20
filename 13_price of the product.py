price=int(input("Enter price of the product :"))
units=int(input("Enter number of units :"))
discount=int(input("Enter discount percentage :"))
tax=int(input("Enter Tax percentage :"))
initial_price=price*units
final_price=initial_price-(discount/100)*initial_price+(tax/100)*initial_price
print("initial price is :",initial_price)
print("final price is :",final_price)