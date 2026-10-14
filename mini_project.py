# RESTAURANT MANAGEMENT SYSTEM PROJECT:-{Hotel menu}
# Use concepts: 
# (i) Dictionary datatype:        (ii) Conditional ststement:

menu = {'Pizza':60,
      'Pasta':50,
      'Burger':80,
      'Salad':70,
      'Coffee':90,
      'pockporn':50,
      'nudals':40
      }

# Greet
print("Welcome to my PYTHON Restaurant", end="\n\n")

print("Pizza: Rs60\nPasta: Rs50\nBurger: Rs80\nSalad: Rs70\nCoffee: Rs90\npockporn: Rs50\nnudals: Rs40")

order_total =0 

item_1 =input("Enter the name of item which you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]# 0+50=50
    print(f"Your item {item_1}  has been added to your order")

else:
    print(f"Please order something else because items is not available yet ")

another_order = input("Do you want add another items? (yes/no)")
if another_order =="yes":
     
     item_2 = input("Enter the name of second item you want to order = ")
     if item_2 in menu:
         order_total += menu[item_2]
         print(f" Item {item_2} has been added to your order: ")

else:
    print(f" Ordered item  is not available!")

print(f"The tatal ammount of items is to pay {order_total}: ")             
