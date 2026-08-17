
"""Login Validation: Ask the user for a username and password. Check whether the username is correct first,
 then check the password"""

user = input("Enter your Username:")
password = input("Enter your password:")

if user == "Siva":
    if password == "1234":
        print("Login Successful")
    else:
        print("Check your Password.")
else:
    print("Check your credentials.")
