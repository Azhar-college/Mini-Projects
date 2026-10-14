# Logic building:
# Take input for Room rent
#  Take input total food order 
# Electricity unit spend 
# Electricity charge per unit
# Peole /persons who leving in room  
# output or result
# Total amount you've to pay is.
rent = int(input("please enter your flat rent:"))

food = int(input("enter the amount of food ordered:="))

electricity_unit_spend = int(input("enter the total of electricity spend:="))
charge_per_unit = int(input("enter the charge electricity per unit:= "))

persons =int(input("enter the people who leving in room or flat:="))

total_bill = electricity_unit_spend * charge_per_unit
output = (rent+food+total_bill)//persons

print("each person will pay = ", output)

