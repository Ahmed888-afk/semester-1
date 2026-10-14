# Worksheet 1.2: Task 1 Solution
import sys
 
text = input("Enter an integer grade (0-100): ").strip()
 
if not text.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")
 
grade = int(text)
 
if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
 
if grade >= 70:
    result = "Distinction"
elif grade >= 40:
    result = "Pass"
else:
    result = "Fail"
 
print(grade, "is a", result)