# CTI-110
# M2HW2 - Tip Tax Total
# Jeremiah James
# 09 SEP 2017
#
foodCost = float(input("Sub-Total: "))
salesTax = .07 * foodCost
tipAmount = .18 * (foodCost + salesTax)
print("Sales Tax:", "%.2f"%(salesTax))
print("Total:", "%.2f"%(foodCost + salesTax))
print("Tip(18%):", "%.2f"%(tipAmount))
print("Total plus Tip:", "%.2f"%(foodCost + salesTax + tipAmount))
