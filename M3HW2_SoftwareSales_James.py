# CTI 110
# M3HW2 - Software Sales
# Jeremiah James
# 24 SEP 2017
#

def main():
    package = 99
    x = int(input("How many software packages would you like to purchase? "))
    cost = package * x
    #discount1 = "%.2f"%(cost * .1)
    #print("Total cost:$",cost)
    if x <= 9:
        print("No discount available.")
        print("Total Cost:$","%.2f"%cost)
    elif x <= 19:
        discount1 = .1 * cost
        print("A discount of 10% is applied.")
        print("Subtotal:$", "%.2f"%cost)
        print("Discount:$", "%.2f"%discount1)
        print("Total Cost:$","%.2f"%(cost - discount1))
    elif x <= 49:
        discount2 = .2 * cost
        print("A discount of 20% is applied.")
        print("Subtotal:$","%.2f"%cost)
        print("Discount:$","%.2f"%discount2)
        print("Total Cost: $","%.2f"%(cost - discount2))
    elif x <= 99:
        discount3 = .3 * cost
        print("A discount of 30% is applied.")
        print("Subtotal:$","%.2f"%cost)
        print("Discount:$","%.2f"%discount3)
        print("Total Cost:$","%.2f"%(cost - discount3))
    else:
        discount4 = .4 * cost
        print("A discount of 40% is applied.")
        print("Subtotal:$","%.2f"%cost)
        print("Discount:$","%.2f"%discount4)
        print("Total Cost:$","%.2f"%(cost - discount4))
    
main()


