import pandas as pd

groceries = pd.read_csv("2 - groceries.csv")
print(groceries)

print()

print(groceries.head(2))

print()

filter = groceries[groceries["value"] > 10]
print(filter)

print()

order = groceries.sort_values("value", ascending = True)
print(order)