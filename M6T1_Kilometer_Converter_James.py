# CTI 110
# M6T1 - Kilometer Converter
# Jeremiah James
# 4 NOV 2017

CONVERSION_FACTOR = .6214

def main():
    kilometers = float(input('Enter a distance in kilometers: '))

    show_miles(kilometers)

def show_miles(km):
    miles = "%.4f"%(km * CONVERSION_FACTOR)
    print(km, 'kilometers equals', miles, 'miles.')
                       

main()
