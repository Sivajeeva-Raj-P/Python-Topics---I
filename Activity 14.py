
# Create a tuple containing numbers with duplicate values. Find how many times 20 occurs and find its first position

numbers = (10,20,30,20,40,50,20,60,70,80,90,20)

# to find how many 20s are there , use count functions
Total = numbers.count(20)

# to find the first position of 20
Position = numbers.index(20)

print("The numbers are:",numbers)
print("The position is:",Position)
print("The number of times 20 repeat is:",Total)