 
name_input = input("Student Name: ")
daily_transport_cost = float(input("Daily Transport Cost: "))
daily_feeding_cost = float(input("Daily Feeding Cost: "))
number_of_days = int(input("Days On Campus: "))
other_expenses = float(input("Other weekly expenses: "))
transport_total = daily_transport_cost * number_of_days
feeding_total = daily_feeding_cost * number_of_days
weekly_total = transport_total + feeding_total + other_expenses
print("WEEKLY EXPENSE SUMMARY")
print(f"Student: {name_input}")
print(f"Transport total: NGN {transport_total:.2f}")
print(f"Feeding total: NGN {feeding_total:.2f}")
print(f"Other expenses: NGN {other_expenses:.2f}")
print(f"Weekly total: NGN {weekly_total:.2f}")

