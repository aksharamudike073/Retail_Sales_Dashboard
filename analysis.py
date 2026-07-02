import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())

import matplotlib.pyplot as plt

df["Category"].value_counts().plot(kind="bar")

plt.title("Products by Category")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()

sales = df.groupby("Category")["Sales"].sum()

sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(6,4))
profit.plot(kind="bar", color="green")

plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()

region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar", color="orange")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()

sub_sales = df.groupby("Sub-Category")["Sales"].sum()

sub_sales.plot(kind="bar", figsize=(12,5), color="purple")

plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

state_sales.plot(kind="bar", color="red", figsize=(10,5))

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()

# Sales by Segment

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(6,5))
segment_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales by Segment")
plt.ylabel("")

plt.show()

# Monthly Sales Trend

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()