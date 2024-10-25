score = int(input("What is your score: "))
grade = "N/A"

if score >= 90:
    grade = "A"
elif score >= 80 < 90:
    grade = "B"
elif score >= 70 < 80:
    grade = "C"
elif score >= 60 < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is ", grade)
