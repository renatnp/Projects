import pandas as pd

purchases = pd.read_csv("2 - groceries.csv")

print("Table:")
print(purchases)

print("\nItem Column:")
print(purchases["item"])

print("\nPrice Column:")
print(purchases["value"])

print("\nQuantity Column:")
print(purchases["quantity"])

average = purchases["value"].mean()
print(f"Average Price: ${average:.2f}")

purchases["total"] = purchases["value"] * purchases["quantity"]
print("\nTable with New Column:")
print(purchases)

total_value = purchases["total"].sum()
print(f"\nTotal Value: ${total_value:.2f}")

total_quantity = purchases["quantity"].sum()
print(f"\nTotal Quantity of Items: {total_quantity}")