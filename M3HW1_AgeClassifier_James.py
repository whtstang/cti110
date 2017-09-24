# CTI-110
# M3HW1 - Age Classifier
# Jeremiah James
# 19 SEP 2017
#

def main():
    age = int(input("How old is this person? "))
    if age <= 1:
        print("This person is an infant.")
    elif age < 13:
        print("This person is a child")
    elif age < 20:
        print("This person is a teenager")
    else:
        print("This person is an adult")

main()
    
