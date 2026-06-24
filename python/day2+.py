import math
from os import system

def main():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
    except ValueError as e:
        print(f"Invalid input: {e}")
        number = 0
        system.exit()
    
    print(f"Square root of {number} is {math.sqrt(number)}")
    print(f"Square of {number} is {math.pow(number, 2)}")
    print(f"Cube of {number} is {math.pow(number, 3)}")

    
if __name__ == "__main__":
    main()
