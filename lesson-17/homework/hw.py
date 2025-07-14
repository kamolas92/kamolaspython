#1
import pandas as pd
import numpy as np

# Create DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Rename columns using a function
def rename_columns(col_name):
    mapping = {
        "First Name": "first_name",
        "Age": "age"
    }
    return mapping.get(col_name, col_name)

df.rename(columns=rename_columns, inplace=True)

# Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# Find mean age
mean_age = df['age'].mean()
print("\nMean age:", mean_age)

# Select and print only 'first_name' and 'City' columns
print("\nSelected columns (first_name and City):")
print(df[['first_name', 'City']])

# Add a new column 'Salary' with random salary values between 50,000 and 120,000
np.random.seed(42)  # for reproducibility
df['Salary'] = np.random.randint(50000, 120001, size=len(df))

# Display summary statistics
print("\nSummary statistics:")
print(df.describe(include='all'))

#2
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

# Display the DataFrame
print("Sales and Expenses DataFrame:")
print(sales_and_expenses)

# Calculate maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

# Calculate minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

# Calculate average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

print(f"\nMaximum Sales: {max_sales}")
print(f"Maximum Expenses: {max_expenses}")
print(f"Minimum Sales: {min_sales}")
print(f"Minimum Expenses: {min_expenses}")
print(f"Average Sales: {avg_sales:.2f}")
print(f"Average Expenses: {avg_expenses:.2f}")

#3
import pandas as pd

# Create the DataFrame
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Set 'Category' as index
expenses.set_index('Category', inplace=True)

# Display the DataFrame
print("Expenses DataFrame with 'Category' as index:")
print(expenses)

# Calculate max expense for each category
max_expenses = expenses.max(axis=1)
print("\nMaximum expense per category:")
print(max_expenses)

# Calculate min expense for each category
min_expenses = expenses.min(axis=1)
print("\nMinimum expense per category:")
print(min_expenses)

# Calculate average expense for each category
avg_expenses = expenses.mean(axis=1)
print("\nAverage expense per category:")
print(avg_expenses)



