import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Undefined for negative numbers"
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        return "Undefined for non-positive numbers"
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")
        
        choice = input("Choose an operation: ")
        
        if choice == '1':
            x = float(input("Enter number: "))
            print(f"√{x} = {square_root(x)}")
        elif choice == '2':
            x = int(input("Enter number: "))
            print(f"{x}! = {factorial(x)}")
        elif choice == '3':
            x = float(input("Enter number: "))
            print(f"ln({x}) = {natural_log(x)}")
        elif choice == '4':
            x = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print(f"{x}^{b} = {power(x, b)}")
        elif choice == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
	main()
