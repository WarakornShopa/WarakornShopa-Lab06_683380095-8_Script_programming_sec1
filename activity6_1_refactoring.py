def positive_negative_zero(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"


def even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


def classify_number(number):
    print(f"{number} is {positive_negative_zero(number)}.")
    print(f"{number} is {even_odd(number)}.")


def main():
    while True:
        user_input = input(
            "\nEnter an integer (or q to quit): "
        ).strip()

        if user_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            number = int(user_input)
            classify_number(number)
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
