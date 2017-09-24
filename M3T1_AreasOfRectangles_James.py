# CTI-110
# M3T1 - Areas of Rectangles
# Jeremiah James
# 18 SEP 2017
#

#Finds the area of rectangle 1
L1 = float(input("Length of rectangle 1: "))
W1 = float(input("Width of rectangle 1: "))
A1 = L1 * W1
#print("Area of rectangle 1:", A1)

#Finds the area of rectangle 2
L2 = float(input("Length of rectangle 2: "))
W2 = float(input("Width of rectangle 2: "))
A2 = L2 * W2
#print("Area of rectangle 2:", A2)

#Compares both rectangles to determine which has larger area or if they are equal     
if A1 > A2:
    print("Rectangle 1 has the larger area.")
elif A2 > A1:
    print("Rectangle 2 has the larger area.")
else:
    print("Both rectangles have equal areas.")
        
