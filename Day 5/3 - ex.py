import pandas as pd

groceries = pd.read_csv("4 - ex.csv")
print(f"Full Table:\n{groceries}\n")

filter = groceries[groceries["value"] > 10]
print(f"Filter 'Value > $10':\n{filter}\n")

second_filter = groceries[groceries["quantity"] > 1]
print(f"Filter 'Quantity > 1':\n{second_filter}\n")

order = groceries.sort_values("total", ascending = False)
print(f"Table sorted by 'total', descending:\n{order}\n")

third_filter = groceries[groceries["value"] == 20.5]
print(f"Filter 'Value = $20.50':\n{third_filter}")