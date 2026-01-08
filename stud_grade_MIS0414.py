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
if marks >= 90:
    category = "Distinction"
elif marks >= 75:
    category = "First Class"
elif marks >= 60:
    category = "Second Class"
else:
    category = "No Class"
print("Category:", category)
