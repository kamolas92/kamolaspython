#Homework1
##1.
category_quantity = salesdata.groupby('Category')['Quantity'].sum().reset_index()
category_quantity = category_quantity.sort_values(by='Quantity', ascending=False)
print(category_quantity)
##2.
avg_price_per_category = salesdata.groupby('Category')['Price'].mean().reset_index()
avg_price_per_category['Price'] = avg_price_per_category['Price'].round(2)
avg_price_per_category = avg_price_per_category.sort_values(by='Price', ascending=False)
print(avg_price_per_category)
##3.
grouped = salesdata.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
grouped_sorted = grouped.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_products = grouped_sorted.drop_duplicates(subset='Category', keep='first').reset_index(drop=True)
top_products
##4.
salesdata['Total_Sales'] = salesdata['Quantity'] * salesdata['Price']
daily_sales = salesdata.groupby('Date')['Total_Sales'].sum().reset_index()
max_sales_date = daily_sales.loc[daily_sales['Total_Sales'].idxmax()]
print("Date with highest total sales:")
print(max_sales_date)
#Homework2
##1.
order_counts = df_customord.groupby('CustomerID')['OrderID'].nunique().reset_index(name='OrderCount')
eligible_customers = order_counts[order_counts['OrderCount'] >= 20]
filtered_df = df_customord[df_customord['CustomerID'].isin(eligible_customers['CustomerID'])]
print(filtered_df.head())
##2.
avg_price_per_customer = df_customord.groupby('CustomerID')['Price'].mean().reset_index()
high_value_customers = avg_price_per_customer[avg_price_per_customer['Price'] > 120]
print(high_value_customers)
##3.
df_customord['Total_Price'] = df_customord['Quantity'] * df_customord['Price']
product_summary = df_customord.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Total_Price', 'sum')
).reset_index()
filtered_products = product_summary[product_summary['Total_Quantity'] >= 5]
print(filtered_products)
#Homework3
##1.
import pandas as pd
import sqlite3

# Read salary band definitions from Excel
salary_band_df = pd.read_excel(r"task\population salary analysis.xlsx")

# Read population data from SQLite
conn = sqlite3.connect(r"task\population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# Assume salary_band_df has columns: 'Band', 'Min', 'Max'
# Assign salary band to each row in population_df
def get_salary_band(salary):
    for _, row in salary_band_df.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Band']
    return 'Other'

population_df['Salary Band'] = population_df['salary'].apply(get_salary_band)

# Total population for percentage calculation
total_population = len(population_df)

# Measures by Salary Band
summary = population_df.groupby('Salary Band').agg(
    Population_Count=('salary', 'count'),
    Average_Salary=('salary', 'mean'),
    Median_Salary=('salary', 'median')
).reset_index()
summary['Percentage_of_Population'] = (summary['Population_Count'] / total_population) * 100

print("Measures by Salary Band:")
print(summary)

# Measures by Salary Band in Each State
state_totals = population_df.groupby('State')['salary'].count().reset_index(name='State_Total')
state_salary_summary = population_df.groupby(['State', 'Salary Band']).agg(
    Population_Count=('salary', 'count'),
    Average_Salary=('salary', 'mean'),
    Median_Salary=('salary', 'median')
).reset_index()
state_salary_summary = state_salary_summary.merge(state_totals, on='State', how='left')
state_salary_summary['Percentage_of_Population'] = (state_salary_summary['Population_Count'] / state_salary_summary['State_Total']) * 100

print("\nMeasures by Salary Band in










