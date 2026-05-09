# Accept an integer and Print hello world n times 
num = int(input("Enter integer :"))
for i in range(num):
    print("Hello")

# Print natural number up to n 
for i in range(1,num+1):
    print(i)

# Reverse for loop. Print n to 1 
n = 5
for i in range(5,0,-1):
    print(i)

# Take a number as input and print its table 
for i in range(11):
    print(num * i)

# Sum up to n terms 
sum = 0
for i in range(num+1):
    sum += i

print(sum)

# Factorial of a number 
fact = 1
for i in range(1,num + 1):
    fact = fact * i
print(fact)

#  Print the sum of all even & odd numbers in a range separately 
even_sum = 0
odd_sum = 0

for i in range(1,num+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    
print("Even sum : " , even_sum)
print("Odd Sum : ", odd_sum)

#  Print all the factors of a number 
for i in range(1,num + 1):
    if num % i == 0:
        print(i)

# Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself
# Ex - 6 = 1, 2, 3 = 6

sum_of_factors = 0

# Loop through numbers from 1 up to (but not including) num
for i in range(1, num):
    if num % i == 0:
        sum_of_factors += i

if sum_of_factors == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is Not perfect")

#  Check wether the number is prime or not 
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is Not a prime number")

# Reverse a string without using in build functions.4
str = "kaif"
rvs = ""
for i in range(len(str) - 1,-1,-1):
    rvs += str[i]
print(rvs)

# Check string is Pallindrome or not 
str = "nayan"
rvs = ""
for i in range(len(str) - 1,-1,-1):
    rvs += str[i]

if rvs == str:
    print(f"{str} is palindromic string")
else:
    print(f"{str} is not a palindromic string")

# Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
char_count = 0
digit_count = 0
symbol_count = 0

for char in str1:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1

print(f"Chars = {char_count}")
print(f"Digits = {digit_count}")
print(f"Symbol = {symbol_count}")

