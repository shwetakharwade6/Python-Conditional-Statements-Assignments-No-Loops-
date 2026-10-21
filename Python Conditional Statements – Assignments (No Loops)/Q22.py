salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years >= 10:
    bonus = salary * 20 / 100
elif years >= 5:
    bonus = salary * 10 / 100
else:
    bonus = salary * 5 / 100

print("Bonus amount is:", bonus)