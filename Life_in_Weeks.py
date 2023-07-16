age = int(input("enter your current age: "))
expected_life_time = int(input("enter your expectancy life time in years: "))

years_left = expected_life_time - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"If you got {expected_life_time} Years in your life time: \n")

print(f"all you left with {years_left} years, {months_left} months, {weeks_left} weeks and {days_left} days")



