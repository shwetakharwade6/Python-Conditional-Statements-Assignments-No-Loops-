username = input("Enter username:")

if username == "admin":
    password = input("Enter password:")

    if password == "12345":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")