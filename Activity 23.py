
# Get 3 numbers and find the largest among them without using max

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
num3 = int(input("Enter another number also:"))

if num1 > num2 and num1 > num3:
    print(str(num1) + " " + "is largest.")
elif num2 > num1 and num2 > num3:
    print(str(num2)+" "+"is largest.")
elif num3 > num1 and num3 > num2:
    print(str(num3)+" "+"is largest.")
elif num1 == num2 == num3:
    print("These numbers are equal")
else:
    print("Error.")
