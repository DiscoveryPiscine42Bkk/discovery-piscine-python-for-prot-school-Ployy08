num = input("Give me a number: ")
if "." in num:
    try:
        float(num)
        print("This number is a decimal.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
else:
    try:
        int(num)
        print("This number is an integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")