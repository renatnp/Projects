# 1. while loop
counter = 1

while counter <= 5:
    print(f"Counting: {counter}")
    counter += 1


# 2. for loop with range()
for i in range(1, 6):
    print(f"Counting: {i}")

total = 0


# 3. Counter and accumulator
for i in range(1, 4):
    grade = float(input(f"Enter grade {i}: "))
    total += grade

average = total / 3
print(f"The average is {average:.2f}")