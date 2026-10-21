attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance >= 75:
    if marks >= 40:
        print("Student is eligible for the exam")
    else:
        print("Student is not eligible due to low marks")
else:
    print("Student is not eligible due to low attendance")