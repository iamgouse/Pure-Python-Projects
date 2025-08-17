from soupsieve import match


print("Welcome to the Simple Calculator!")
print("Please enter your calculations in the format: number1 operator number2")
print("Supported operators: +, -, *, /")

while True:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    n = input("Enter operation: ")
    match(n):
        case "+":
                print(f"Addition of two numbers is {a+b}")
                break
        case "-":
                print(f"Subtraction of two numbers is {a-b}")
                break
        case "*":
                print(f"Multiplication of two numbers is {a*b}")
                break
        case "/":
                print(f"Division of two numbers is {a//b}")
                break

        case _:
              print("Use valid operator mentioned above")
              break
       
