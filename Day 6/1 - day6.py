import pandas as pd

groceries = pd.read_csv("2 - simulation.csv")
print(f"Full table:\n{groceries}\n")

filter = groceries[(groceries["value"] > 10) | (groceries["quantity"] > 1)]
print(f"Filter 'Value > 10 or Quantity > 1':\n{filter}\n")

second_filter = groceries[(groceries["value"] > 10) & (groceries["quantity"] > 1)]
print(f"Filter 'Value > 10 and Quantity > 1':\n{second_filter}\n")

print(f"Number of rows in the first filter: {filter.shape[0]}")

print(f"Number of rows in the second filter: {len(second_filter)}")

print("Number of items per category:")
print(groceries["category"].value_counts())

print("\nItems from 'condiments' and 'vegetables' categories:")
print(groceries[groceries["category"].isin(["condiments", "vegetables"])])