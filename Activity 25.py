
""" Calculate an electricity Bill based on units consumed ...Upto 100 units => 5 rupees/unit , 101 - 200 units => 7 rupees/unit
  Above 200 units => 10 rupees/unit"""

name = input("Enter the consumer name:")
units = int(input("Please enter the units consumed:"))

if units <= 100:
    total = units * 5
    print(name + " " + "wants to paid"+" "+str(total))
elif units <= 200 and units >= 101:
    total = units * 7
    print(name + " " + "wants to paid"+" "+str(total))
else:
        total = units * 10
        print(name + " " + "wants to paid" + " " + str(total))