# CTI 110
# M6T2 - Feet to Inches Converter
# Jeremiah James
# 4 NOV 2017

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Number of feet to convert: '))
                     
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
                     


def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
    

main()
                       
