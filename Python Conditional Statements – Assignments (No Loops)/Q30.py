num = int(input("Enter a number:"))

if num >= -9 and num <= 9:
    print("The number is a single-digit number")
elif num >= -99 and num <= 99:
    print("The number is a double-digit number")
elif num >= -999 and num <= 999:
    print("The number is a three-digit number")
else:
    print("The number has more than three digits")