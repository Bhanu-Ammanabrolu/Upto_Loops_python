year = int(input("Which Year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is A LEAP YEAR")
        else:
            print(f"{year} is NOT A LEAP YEAR")
    else:
        print(f"{year} is A LEAP YEAR")
else:
    print(f"{year} is NOT A LEAP YEAR")

