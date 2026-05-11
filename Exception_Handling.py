# Errors occur due to mistakes in the code that prevent it from
# running. These can be syntax errors or logical errors

# Exceptions are unexpected events or errors that occurs
# during the execution of a program, which disrupts the normal
# flow of the program.

# try : This block contains code that may raise an exception.
# except : This block handles the exception if it occurs. You can specify.
# else : This block executes if no exceptions are raised in the try block.
# finally : This block executes regardless of whether an exception occurred or not.
# raise : This statement is used to manually raise an exception.

num = int(input("Enter a number: "))
try:
    result = 5 / num
    print("The result is:", result)

except Exception as e:
    print("Error: You cannot divide by zero!")

else:
    print("Division successful!")

finally:
    print("This block will always execute.")