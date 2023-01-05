print("Welcome to the tip calculator.\n")
total_bill = input("What was the total bills? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
split_number = input("How many people to split the bill? ")

total_with_tip = float(total_bill) + (float(total_bill) * float(f"0.{percentage_tip}"))

total_each_person = (total_with_tip) / int(split_number)
print(f"Each person should pay: ${round(total_each_person, 2)}")