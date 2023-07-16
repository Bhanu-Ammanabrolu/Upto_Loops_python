number = int(input("Enter a number to check for Even_Odd: "))

if number <= 0:
    print(f"The given number is {number} - INVALID!")
elif number % 2 == 0:
    print(f"{number} is an EVEN Number")
else:
    print(f"{number} is ODD number")
