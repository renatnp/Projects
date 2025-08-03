# 1. Lists
grades = [8.5, 7.0, 9.2]
names = ["Ana", "Carlos", "Renato"]
ages = [16, 17, 18]

print(grades[0])
print(names[2])

grades.append(7.5)
grades.pop(0)
print(grades)

# 2. Looping through lists with for
for grade in grades:
    print(f"Grade: {grade:.2f}")

for i in range(len(grades)):
    print(f"Grade {i+1}: {grades[i]:.2f}")