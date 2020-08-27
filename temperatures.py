"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_degrees_to_farenheit():
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_farenheit_to_degrees():
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_degrees_to_farenheit()

        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Farenheit: "))
        celsius = convert_farenheit_to_degrees()
        print("Result: {:.2f} C".format(celsius))
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
