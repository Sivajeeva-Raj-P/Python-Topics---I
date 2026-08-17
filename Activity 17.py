
""" Create a dictionary containing product information. Display the product name and price. Try to access a key that
doesn't exist without causing error."""

prdt = {
    "productname" : "Laptop",
    "price": 65760,
    "brand": "Dell"
}
print("The product name is:",prdt["productname"])
print("The price of the product is:",prdt["price"])
print("The BrandName of the product is:",prdt["brand"])

print("stock:",prdt.get("stock","Not Available"))