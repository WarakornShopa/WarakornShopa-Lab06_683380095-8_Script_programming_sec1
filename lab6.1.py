def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base, exponent=2):
    return base ** exponent


def main():
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (**)")
        print("0. Exit")

        choice = input("Choose an operation (0-5): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice. Please choose 0-5.")
            continue

        try:
            first = float(input("Enter the first number: "))
            if choice == "5":
                exponent_text = input(
                    "Enter exponent (press Enter to square): "
                ).strip()
                if exponent_text == "":
                    result = power(first)
                else:
                    result = power(first, float(exponent_text))
            else:
                second = float(input("Enter the second number: "))

                if choice == "1":
                    result = add(first, second)
                elif choice == "2":
                    result = subtract(first, second)
                elif choice == "3":
                    result = multiply(first, second)
                else:
                    result = divide(first, second)

            print("Result:", result)

        except ValueError:
            print("Invalid number. Please enter a numeric value.")


if __name__ == "__main__":
    main()
