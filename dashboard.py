import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Create dashboard
plt.figure(figsize=(15,10))

# 1. Products by Category
plt.subplot(2,2,1)
df["Category"].value_counts().plot(kind="bar")
plt.title("Products by Category")

# 2. Sales by Region
plt.subplot(2,2,2)
df.groupby("Region")["Sales"].sum().plot(kind="bar", color="orange")
plt.title("Sales by Region")

# 3. Profit by Category
plt.subplot(2,2,3)
df.groupby("Category")["Profit"].sum().plot(kind="bar", color="green")
plt.title("Profit by Category")

# 4. Top 10 States by Sales
plt.subplot(2,2,4)
df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10).plot(kind="bar", color="red")
plt.title("Top 10 States by Sales")

plt.tight_layout()
plt.show()