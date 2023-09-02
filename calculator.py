
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Unable to divide by zero"
    return x / y

while True:
  
    try:
        print("**********Welcome to Calculator************")
        num1 = float(input("Enter first number:- "))
        num2 = float(input("Enter second number:- "))
    except ValueError:
        print("\nInvalid input.")
        print("Please enter numeric values.")
        continue

    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
   

    operation = input("Enter operation (1/2/3/4): ")

    

    if operation not in ('1', '2', '3', '4'):
        print("\nInvalid operation.")
        print("Please select a valid operation.")
        continue

    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)

    print("Result:- ", result)
