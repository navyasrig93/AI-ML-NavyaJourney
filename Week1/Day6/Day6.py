import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#print("Matplotlib installed successfully.")

# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# sales = [1200, 1500, 1700, 2200, 2500]

# plt.plot(months, sales)

# plt.title("Monthly Sales Trend")
# plt.xlabel("Months")
# plt.ylabel("Sales")

# plt.show()

# departments = ["IT", "HR", "Finance", "Marketing"]
# employees = [15, 5, 8, 6]

# plt.bar(departments, employees)
# plt.title("Number of Employees per Department")
# plt.xlabel("Deparments")
# plt.ylabel("Number of Employees")

# plt.show()

# scores = [70,75,80,82,85,88,90,92,95,98]

# plt.hist(scores)

# plt.title("Student Score Distribution")

# plt.show()

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# profit = [500, 700, 600, 900, 1200, 1400]

# plt.title("Monthly Profit Trend")
# plt.xlabel("Months")
# plt.ylabel("Profit")
# plt.plot(months, profit, marker = 'o')
# plt.grid(True)
# plt.show()

months = ["Jan","Feb","Mar","Apr","May","Jun"]

sales = [1000,1200,1500,1700,2100,2500]

df = pd.DataFrame({"Months": months, "Sales": sales})

print(df)

total_sales = df["Sales"].sum()
print(f"Total Sales: {total_sales}")

avg_sales = df["Sales"].mean()
print(f"Average Sales: {avg_sales}")

highest_sales = df["Sales"].max()
print(f"Highest Sales: {highest_sales}")
print(f"Month with Highest Sales: {df.loc[df['Sales'].idxmax(), 'Months']}")

lowest_sales = df["Sales"].min()
print(f"Lowest Sales: {lowest_sales}")
print(f"Month with Lowest Sales: {df.loc[df['Sales'].idxmin(), 'Months']}")

plt.plot(months, sales)
plt.title("Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
plt.bar(months, sales)
plt.title("Sales by Month")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 1. Sales increased steadily throughout the period.
# 2. June had the highest sales.
# 3. Average sales exceeded 1600.

if sales[-1] > sales[0]:
    print("Sales increased steadily throughout the period.")
if sales[-1] == highest_sales:
    print("June had the highest sales.")
if avg_sales > 1600:
    print("Average sales exceeded 1600.")

