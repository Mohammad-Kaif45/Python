# Separate each digit of a number and print it on the new line

num = 12345
digits = []

while num > 0:
    digit = num % 10      # Get the last digit
    digits.append(digit)  # Store it
    num = num // 10       # Remove the last digit

# Reverse the list and print
for d in reversed(digits):
    print(d)
