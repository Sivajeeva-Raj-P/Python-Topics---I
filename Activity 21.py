
# Get a number from the user and determine whether it is positive,negative or zero

number = int(input("Enter a number:"))

def check(num):
    if num > 0:
        print("The number is Positive",num)
    elif num < 0:
        print("The number is negative",num)
    else:
        print("The number is zero",num)

check(number)