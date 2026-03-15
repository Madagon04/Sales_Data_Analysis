import pandas as pd
import matplotlib.pyplot as plt
# Read the  dataset
data = pd.read_csv("sales_data.csv")
# Create the Total column
data["Total"] = data["Quantity"] * data["Price"]
print("\n================ SALES DATA ================\n")
print(data)
# Total revenue
total_rev = data["Total"].sum()
print("\n============================================")
print("Total Revenue:", total_rev)
print("============================================")
# Sales by product
product_sales = data.groupby("Product")["Total"].sum()
print("\n----------- Sales by Product -----------")
for product, revenue in product_sales.items():
    print(f"{product:<10} : {revenue}")
# Best-selling product
best_pro = product_sales.idxmax()
print("\nBest Selling Product:", best_pro)
# Total Quantity sold
quantity = data.groupby("Product")["Quantity"].sum()
print("\n------- Total Quantity Sold -------")
for product, qty in quantity.items():
    print(f"{product:<10} : {qty}")
# Bar chart of product and revenue
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
# Pie chart
quantity.plot(kind="pie", autopct="%1.1f%%")
plt.title("Product Sales Distribution")
plt.ylabel("")
plt.show()
