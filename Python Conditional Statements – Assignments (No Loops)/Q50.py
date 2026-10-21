print("ATM Menu")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4):"))

match choice:
    case 1:
        print("Your balance is Rs. 5000")
    case 2:
        amount = float(input("Enter deposit amount:"))
        if amount > 0:
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")
    case 3:
        amount = float(input("Enter withdrawal amount:"))
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= 5000:
            print("Please collect your cash:", amount)
        else:
            print("Insufficient balance")
    case 4:
        print("Thank you for using our ATM")
    case _:
        print("Invalid choice")