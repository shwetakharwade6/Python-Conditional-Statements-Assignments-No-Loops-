sub1 = int(input("Enter marks for subject 1:"))
sub2 = int(input("Enter marks for subject 2:"))
sub3 = int(input("Enter marks for subject 3:"))

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
    print("Student passed all subjects")
else:
    print("Student failed in one or more subjects")