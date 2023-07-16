import random

names_string = input("Enter names separated by comma. ")
list_of_names = names_string.split(", ")

print(f"given names are {list_of_names}")
persons = len(list_of_names)

bill_payer_index = random.randint(0, persons - 1)

print(f"{list_of_names[bill_payer_index]} is going to pay the bill today. HURRAY")