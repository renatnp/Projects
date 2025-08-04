import pandas as pd

purchases = pd.read_csv("simulation.csv")

print("Full table:")
print(purchases)

print("\nValue column:")
print(purchases["value"])

average = purchases["value"].mean()
print(f"\nAverage value: ${average:.2f}")

purchases["total"] = purchases["value"] * purchases["quantity"]

print("\nTable with 'total' column:")
print(purchases)

total_spent = purchases["total"].sum()
print(f"\nTotal amount spent: ${total_spent:.2f}")