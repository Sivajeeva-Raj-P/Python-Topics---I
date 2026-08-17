
# Create a function that accepts the price and discount percentage and returns the final price.

price = int(input("Enter the Price of the product:"))
discount = int(input("Enter the discount percentage :"))

def finalprice(amount,discount):

    Discountamount = amount * (discount / 100)
    FinalPrice = amount - Discountamount
    print("The total price for the product is:",FinalPrice)

finalprice(price,discount)

