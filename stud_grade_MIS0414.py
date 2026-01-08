marks = int(input("Enter student marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
if marks >= 90:
    grade = "Outstanding"
elif marks >= 80:
    grade = "Excellent"
elif marks >= 70:
    grade = "Good"
elif marks >= 60:
    grade = "Average"
elif marks >= 50:
    grade = "Fair"
else:
    grade = "Fail"
print("Grade:", grade)
