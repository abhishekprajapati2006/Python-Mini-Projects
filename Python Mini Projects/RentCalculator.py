rent = int(input("Enter Your Hostel/Flat Rent : "))
food = int(input("Enter the Amount of Food Ordered : "))
electricity_spend = int(input("Enter the Total of Electricity Spend : "))
charge_per_unit = int(input("Enter the Charge Per Unit : "))
person = int(input("Enter the Number of People in room/flat : "))

total_electricity_bill = (electricity_spend * charge_per_unit )
one_pay_person = (rent + food + total_electricity_bill) / person
print("Each Person of Pay ₹ ",one_pay_person)