counter = 1
while counter <= 10:
    print(f"Counting: {counter}")
    counter += 1

for counter in range(1, 11):
    print(f"Counting: {counter}")

total = 0
for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    total += grade
average = total / 5
print(f"The average is: {average:.2f}")

for i in range(10, -1, -1):
    print(f"Countdown: {i}")

even_count = 0
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    if num % 2 == 0:
        even_count += 1
print(f"You entered {even_count} even numbers.")