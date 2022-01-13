import pandas as pd
import matplotlib.pyplot as plt

# Creating a data frame using pandas
df = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set.csv')

# Adding and positioning a column to represent average value of a pair of sneakers within each distinct order
df['ASV_perOrder'] = df.apply(lambda row: row.order_amount / row.total_items, axis=1)
column_to_move = df.pop('ASV_perOrder')
df.insert(5, 'ASV_perOrder', column_to_move)

# Data frame print options for review.
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
#print(df)

# Calculating the Average Order Value
AOV = df['order_amount'].mean()

# Calculating the Average Sneaker Value across all orders
ASV = df['order_amount'].sum() / df['total_items'].sum()

Order_median = df['order_amount'].median()
Order_25 = df['order_amount'].quantile(0.25)
Order_75 = df['order_amount'].quantile(0.75)

print("Average sneaker retail value =", ASV)
print("Average order value =", AOV)
print("Order median value =", Order_median)
print("Order 25th % value =", Order_25)
print("Order 75th % value =", Order_75)

# Creating a Multi Boxplot for Order Value and Average Sneaker Value per Order
columns = [df['order_amount'], df['ASV_perOrder']]

fig, ax = plt.subplots()

# Establishing the boxplots without outliers and with the whiskers stretched to the 2.5 and 97.5 percentiles
ax.boxplot(columns, showfliers=False, whis = [2.5, 97.5])

# Establishing the annotations and aesthetics for the boxplots
plt.title('Box Plots of Order Amounts \nand Average Sneaker Value Per Order')
plt.ylabel('Dollars $')
plt.xticks([1, 2], ["Order Amounts", "Average Sneaker\nValue Per Order"])
ax.text(.65, .95, "Note:\nOutliers are excluded\nfrom these plots", transform=ax.transAxes, ha="left", va="top")
ax.text(.11, .085, "2.5%", transform=ax.transAxes, ha="left", va="top")
ax.text(.11, .16, "25%", transform=ax.transAxes, ha="left", va="top")
ax.text(.09, .32, "Median", transform=ax.transAxes, ha="left", va="top")
ax.text(.11, .46, "75%", transform=ax.transAxes, ha="left", va="top")
ax.text(.11, .96, "97.5%", transform=ax.transAxes, ha="left", va="top")
plt.show()