# 1. Ask the user to input an odd integer
n = int(input("Enter an odd integer: "))
# 2. Condition to check if the number entered is odd
if n % 2 == 0:
    print("Please provide an odd integer.")
else:
    for i in range(n // 2 + 1):  # Looping for the upper part
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))
    for i in range(n // 2 - 1, -1, -1): # Looping for the lower part
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))