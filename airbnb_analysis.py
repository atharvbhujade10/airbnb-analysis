import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv('mini_airbnb_limited.csv')

# Step 2: Display the dataset
print("Dataset:")
print(df)

# Step 3: Data Visualization

# 3.1 Histogram of Prices
plt.figure(figsize=(6, 4))
plt.hist(df['price'], bins=4, color='skyblue', edgecolor='black')
plt.title('Distribution of Prices')
plt.xlabel('Price (in USD)')
plt.ylabel('Frequency')
plt.show()

# 3.2 Box Plot of Prices
plt.figure(figsize=(6, 4))
plt.boxplot(df['price'], vert=False)
plt.title('Box Plot of Prices')
plt.xlabel('Price (in USD)')
plt.show()

# 3.3 Scatter Plot (Assuming IDs for x-axis)
plt.figure(figsize=(6, 4))
plt.scatter(df['id'], df['price'], color='purple')
plt.title('Scatter Plot of Price vs. ID')
plt.xlabel('ID')
plt.ylabel('Price (in USD)')
plt.show()

# Step 4: Summary Statistics for Price
average_price = df['price'].mean()
max_price = df['price'].max()
min_price = df['price'].min()

print(f"\nAverage Price: ${average_price:.2f}")
print(f"Maximum Price: ${max_price}")
print(f"Minimum Price: ${min_price}")
