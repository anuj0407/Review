# Task 6[anuj]: Function Calculator + File Logging
# Define add, subtract, multiply, divide.
# Use inputs 10,5.
# Save results into calc.txt.
# Read and print file.

try :
    with open("calc.txt","w+") as f:
        num1 = 10
        num2 = 5
        #add function
        def add(a,b):
            return a+b
        #subtract function
        def subtract(a,b):
            return a-b
        #multiply function
        def multiply(a,b):
            return a*b
        #divide function
        def divide(a,b):
            return a/b
        
        operation = input("Write a Operation:(+,-,*,/): ")
        result = 0
        if(operation == '+'):
            result = add(num1,num2)
            f.write(f"addition of {num1} and {num2} is {result}")
        elif(operation == '-'):
            result = subtract(num1,num2)
            f.write(f"subtraction of {num1} and {num2} is {result}")
        elif(operation == '*'):
            result = multiply(num1,num2)
            f.write(f"multiplication of {num1} and {num2} is {result}")
        elif(operation == '/'):
            result = divide(num1,num2)
            f.write(f"division of {num1} and {num2} is {result}")
        else:
            print("Invalid Operation !")

except Exception:
    print("Exception occured")



