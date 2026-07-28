# day1_converter.py
# Goal: convert between Celsius and Fahrenheit based on user input

# TODO 1: Ask which direction with input()
choice = (
    input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ")
    .strip()
    .upper()
)

# TODO 2: Ask for the number with float(input())
number = float(input("Enter the number: "))

# TODO 3 & 4: if/elif logic and result printing
if choice == "C":
    converted = number * 9 / 5 + 32
    print(f"{number}° Celsius is {converted}° Fahrenheit")
elif choice == "F":
    converted = (number - 32) * 5 / 9
    print(f"{number}° Fahrenheit is {converted}° Celsius")
else:
    print("Invalid choice. Please run the program again and enter 'C' or 'F'.")
