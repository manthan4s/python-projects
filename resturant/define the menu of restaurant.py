#enter the menu of the restaurant 
menu={
    "burger":100
    ,"pizza":134
    ,"pasta":1234
    ,"coke":23
}
print("Welcome to our Resturant, Here is our menu")
print('')
print("burger:100\npizza:134\npasta:1234\ncoke:23")
      

Order1 = input("What do you want to order? : ")

print("Your bill is: ", menu[Order1])
Order2 = input("Do you want to order more? : ")
if(Order1 != "Coffe" and Order2 == "No"):
    print("Your total bill is ", menu[Order1] )
    
elif(Order1 == "Coffe" and Order2 == "No"):
    print("Sorry sir, You Cant order just a coffe")
    print("Thank You")

else:
    total_bill = menu[Order1]+menu[Order2]
    Coupon = (input("Do you have a coupon Code, if yes then enter it? :"))
    if(Coupon == "manthan20"):
        disc_value = total_bill * menu[order1]

        print("Your bill after 20% Discount: ", total_bill - disc_value)
    else:
        print("Your total bill is: ", menu[Order1]+menu[Order2])
    
print("Thank you for ordering")
print("please visit again")

#end of the code