status = int(input("Enter result status code (1-4):"))

match status:
    case 1:
        print("Result: Pass")
    case 2:
        print("Result: Fail")
    case 3:
        print("Result: ATKT")
    case 4:
        print("Result: Pending")
    case _:
        print("Invalid status code")