grades = []

for i in range(4):
    grade = float(input(f"Enter the grade for test #{i+1}: "))
    grades.append(grade)

for grade in grades:
    print(f"Grade: {grade:.2f}")

total = sum(grades)

average = total / 4
print(f"Average: {average:.2f}")