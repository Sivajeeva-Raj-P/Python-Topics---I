
# Get a number from 1 t0 7 and display the corresponding day using match

day = int(input("Enter the day number:"))

match day:
        case 1:
            print("The day is monday.")
        case 2:
            print("The day is Tuesday.")
        case 3:
            print("The day is Wednesday.")
        case 4:
            print("The day is Thursday.")
        case 5:
            print("The day is Friday.")
        case 6:
            print("The day is Saturday.")
        case 7:
            print("The day is Sunday,")
        case _:
            print ("Invalid data")
