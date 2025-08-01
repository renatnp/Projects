name = input("Enter your name: ")
birth_date = input("Enter your birth date: ")
print(f"Hello, {name}! You were born on {birth_date}.")

grade = float(input("Enter your grade: "))
print(f"Grade: {grade:.2f}")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))
average = (grade1 + grade2) / 2
if average >= 7:
    print(f"Passed, average: {average:.2f}")
elif average >= 5:
    print(f"Recovery, average: {average:.2f}")
else:
    print(f"Failed, average: {average:.2f}")