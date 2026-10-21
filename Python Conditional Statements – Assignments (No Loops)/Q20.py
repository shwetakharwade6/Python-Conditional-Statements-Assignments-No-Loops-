age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is free")
elif age < 18:
    print("Ticket price is Rs. 50")
elif age < 60:
    print("Ticket price is Rs. 100")
else:
    print("Ticket price is Rs. 50")