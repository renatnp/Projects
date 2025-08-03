# 1. input()
name = input("Enter your name: ")
birth_date = input("Enter your birth date (e.g., 01/01/2000): ")
print(f"Hello, {name}! You were born on {birth_date}.")

grade = float(input("Enter your grade: "))
print(f"Grade: {grade:.2f}")


# 2. if, else and elif
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
average = (grade1 + grade2) / 2
if average >= 7:
    print(f"Passed, average: {average:.2f}")
elif average >= 5:
    print(f"In recovery, average: {average:.2f}")
else:
    print(f"Failed, average: {average:.2f}")
