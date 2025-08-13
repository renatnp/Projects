import pandas as pd

groceries = pd.read_csv("2 - simulation.csv")
print(f"Table:\n{groceries}\n")

sorted_df = groceries.sort_values(by="price", ascending=False)
print(f"Descending order by 'price' column:\n{sorted_df}\n")

print(f"Only 'product' and 'price' columns:\n{groceries[['product', 'price']]}\n")

print(
    f"Only 'product' and 'price' columns sorted in ascending order by 'price' column:\n"
    f"{groceries.sort_values(by='price', ascending=True)[['product', 'price']]}"
)