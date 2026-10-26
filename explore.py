import pandas as pd

df = pd.read_csv("data/superstore.csv", encoding="latin-1")
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
nb_orders = df["Order ID"].nunique()
margin = total_profit / total_sales * 100

print(f"Ventes totales : {total_sales:,.0f}")
print(f"Profit total : {total_profit:,.0f}")
print(f"Nombre de commandes : {nb_orders}")
print(f"Marge : {margin:.1f} %")

sales_by_year = df.groupby(df["Order Date"].dt.year)["Sales"].sum()
print(sales_by_year)

by_category = df.groupby("Category")[["Sales", "Profit"]].sum()
print(by_category)