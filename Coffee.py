#Make a menu
menu = f"coffee \n sugar \n cake"
def reciept_add(main_price,side_price)
#greet the customer Done
print("Welcome In" + "\n" + "Here is the Menu" +"\n" + menu)

""" Take their order make
 Ask for sides """

name = input("What is your name?"+"\n")
main = input("What Coffee would you like" + "\n")
sides = input("Would you like sides? Y/N"+"\n")
side_1 = None
side_2 = None
    if side_1==None: #Finish this Next time needs to get menu price
        side_price1=0
    elif side_2==None:
        side_price2=0
    elif side_1 or side_2 not None
main_price=2.0
sides_price=side_price1+side_price2

try:
    if sides.upper() == "Y":
        side1_price = 0.5
        side2_price = 0.25
        side_1 = input("First Side?" + "\n")
        side_2 = input("Second Side?" + "\n" + "if none type None" + "\n")
    else:
        print(f"Name: {name}\nMain:\n{main})
except Exception as e:
    print(f"An error occurred: {e}")
    
reciept = f"Name: {name}\nMain:\n{main}\nSides:\n{side_1}\n{side_2}"

print(f"\nHeres your reciept\n{reciept}")    

total_price = main_price + side1_price + side2_price

print(f"Total: {total_price}")
