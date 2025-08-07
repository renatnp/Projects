import pandas as pd

groceries = pd.read_csv("2 - simulation.csv")

filter = groceries[groceries["quantity"] > 2]
print(f"Filter 'Quantity > 2':\n{filter}\n")

second_filter = groceries[(groceries["value"] > 10) & (groceries["category"] == "condiments")]
print(f"Filter 'Value > 10 and Category == condiments':\n{second_filter}\n")