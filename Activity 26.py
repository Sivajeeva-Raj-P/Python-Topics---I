
# Create a calculator using match. Get 2 numbers and an operator(+,-,*,/) from the user

num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
operation = input("Enter operator(+,-*,/): ")

match operation:
    case "+":
        sum = num1 + num2
        print("Sum of numbers is:",sum)
    case "-":
        difference = num1 - num2
        print("Difference of numbers is:",difference)
    case "*":
        product = num1 * num2
        print("Product of  numbers is:",product)
    case "/":
        if num2 > 0:
           quotient = num1 / num2
           remainder = num1 % num2
           print("Quotient and Remainder of numbers is;",quotient,remainder)
        else:
            print("Please enter a second number greater than zero.")
    case "_":
        print("Operator not recognized.")