def greet(name):
    print(f"Hello, {name}!")


def is_prime(number):
    if not isinstance(number, int) or isinstance(number, bool):
        return False
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True
