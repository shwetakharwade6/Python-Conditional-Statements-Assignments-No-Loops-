age = int(input("Enter your age:"))
salary = float(input("Enter your monthly salary:"))

if age >= 21:
    if salary >= 25000:
        print("You can apply for a loan")
    else:
        print("You cannot apply due to low salary")
else:
    print("You cannot apply due to age")