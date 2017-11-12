Integer = int(input("Enter a nonnegative integer? "))

while Integer < 1:
    Integer = int(input("Please enter a positve number: "))
print()
factorial = 1

for currentNumber in range(1, Integer + 1):
    factorial = factorial * currentNumber

print("The factorial of", Integer, "is", factorial)
