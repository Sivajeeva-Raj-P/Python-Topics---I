
"""Create a function that accepts a number and returns whether it is a positive even, positive odd,
negative even,negative odd or zero."""

number = int(input("Enter a number:"))

def check(num):
    if num % 2 == 0 and num > 0:
        print("The number is positive even.")
    elif num % 2 != 0 and num > 0:
        print("The number is positive odd.")
    elif num % 2 == 0 and num < 0:
        print("The number is negative even.")
    elif num == 0:
        print("Zero is a positive even number")
    else:
        print("The number is negative odd.")

check(number)