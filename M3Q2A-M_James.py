# CTI 110
# Question M3Q2A-M
# Jeremiah James
# 24 SEP 2017
#

def main():
    x = float(input("What is the temperature (F) of the sample? "))
    if x <= 32:
        print("Solid")
    elif x <= 212:
        print("Liquid")
    else: 
        print("Gas")


main()
    
