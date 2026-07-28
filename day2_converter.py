while True:
    # TODO 1: ask "Convert (C)elsius to Fahrenheit, (F)ahrenheit to Celsius, or (Q)uit? "
    choice = (
        input(
            "Convert (C)elsius to Fahrenheit, (F)ahrenheit to Celsius, or (Q)uit? "
        )
        .strip()
        .upper()
    )

    # TODO 2: if the answer is "Q" or "q", print a goodbye message and break out of the loop
    if choice == "Q":
        print("Goodbye! Thanks for using the converter.")
        break

    # TODO 3: otherwise, run your existing conversion logic from yesterday
    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.1f}°F\n")

    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F is equal to {celsius:.1f}°C\n")

    else:
        print("Invalid choice. Please enter C, F, or Q.\n")
