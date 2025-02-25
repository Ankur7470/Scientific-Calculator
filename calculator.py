import math

def square_root(x):
    """
    Calculate the square root of a number.
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def factorial(x):
    """
    Calculate the factorial of a number.
    """
    if x < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    return math.factorial(x)

def natural_logarithm(x):
    """
    Calculate the natural logarithm (base e) of a number.
    """
    if x <= 0:
        raise ValueError("Cannot calculate natural logarithm of a non-positive number.")
    return math.log(x)

def power_function(x, b):
    """
    Calculate the power of x raised to b.
    """
    return math.pow(x, b)

def display_menu():
    """
    Display the menu options for the calculator.
    """
    print("\nScientific Calculator Menu:")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")
    print("5. Exit")

def main():
    """
    Main function to run the calculator.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            x = float(input("Enter a number to find its square root: "))
            try:
                result = square_root(x)
                print(f"Square root of {x} is: {result}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            x = int(input("Enter a number to find its factorial: "))
            try:
                result = factorial(x)
                print(f"Factorial of {x} is: {result}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            x = float(input("Enter a number to find its natural logarithm: "))
            try:
                result = natural_logarithm(x)
                print(f"Natural logarithm of {x} is: {result}")
            except ValueError as e:
                print(e)

        elif choice == '4':
            x = float(input("Enter the base (x): "))
            b = float(input("Enter the exponent (b): "))
            result = power_function(x, b)
            print(f"{x} raised to the power of {b} is: {result}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
