import math
import random
import lab6_2.my_utils as my_utils

print("===== Custom Module =====")
my_utils.greet("Alice")

for number in (7, 10, 13, 1):
    print(f"Is {number} prime? {my_utils.is_prime(number)}")

print("\n===== math module =====")
number = 81
print(f"Square root of {number} = {math.sqrt(number)}")

print("\n===== random module =====")
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
