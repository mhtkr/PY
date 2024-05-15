#Experiment - 10

while True:
    try:
        num1 = float(input("Enter the first number - "))
        num2 = float(input("Enter the second number - "))

        result = num1 / num2

        print(f"The result of {num1} divided by {num2} is: {result}")

        break
    except ValueError:
        print("Invalid Input, Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divided by zero enter a non zero second number")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
