def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print("Result:", result)
        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print("Result:", result)
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print("Result:", result)
        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)
        elif choice == '5':
            factorial = 1
            num = int(input("Enter the number: "))
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
            elif num == 0:
                print("1")
            else:
                for i in range(1, num + 1):
                    factorial *= i
                print(f"The factorial of {num} is {factorial}")
        elif choice == '6':
            print("Exiting the calculator...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

        print()  # Print an empty line for better readability

# Run the calculator
if __name__ == '__main__':
    calculator()
