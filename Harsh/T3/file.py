import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a random dataset
np.random.seed(0)  # For reproducibility

# Generate a sample dataset
data = {
    'Age': np.random.randint(18, 70, 100),  # Random ages between 18 and 70
    'Income': np.random.randint(30000, 100000, 100),  # Random income between 30k and 100k
    'Spending_Score': np.random.randint(1, 100, 100),  # Random spending score between 1 and 100
    'Category': np.random.choice(['A', 'B', 'C'], 100)  # Random categories A, B, C
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Explore the dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nData types and missing values:")
print(df.info())

# Step 3: Clean the data
# For simplicity, let's assume there's no missing data or duplicate entries in this synthetic data.

# Step 4: Perform analysis
# Group by category and calculate mean income and spending score
category_stats = df.groupby('Category')[['Income', 'Spending_Score']].mean()
print("\nCategory statistics (mean income and spending score):")
print(category_stats)

# Step 5: Visualize the data
# Plotting income distribution
plt.figure(figsize=(10, 5))
plt.hist(df['Income'], bins=20, color='skyblue', edgecolor='black')
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plotting spending score by category
plt.figure(figsize=(10, 5))
df.groupby('Category')['Spending_Score'].mean().plot(kind='bar', color=['red', 'green', 'blue'])
plt.title('Average Spending Score by Category')
plt.xlabel('Category')
plt.ylabel('Average Spending Score')
plt.grid(True)
plt.show()

# Scatter plot: Age vs Income
plt.figure(figsize=(10, 5))
plt.scatter(df['Age'], df['Income'], alpha=0.5, color='purple')
plt.title('Age vs Income')
plt.xlabel('Age')
plt.ylabel('Income')
plt.grid(True)
plt.show()
