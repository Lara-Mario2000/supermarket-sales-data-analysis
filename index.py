import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/Sample-Superstore.csv', encoding='Latin-1')

print(df.head())
print(df.info())
print(df.isnull().sum())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year
df['Order Day of Week'] = df['Order Date'].dt.dayofweek
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

print(df.head())

#trends of sales in months and years
sales_months_years = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(sales_months_years['Order Year'].astype(str) + '-' + sales_months_years['Order Month'].astype(str).str.zfill(2), sales_months_years['Sales'])
plt.plot(sales_months_years['Order Year'].astype(str) + '-' + sales_months_years['Order Month'].astype(str).str.zfill(2), sales_months_years['Sales'], '-o', color='black')
plt.xlabel('Year-Month')
plt.ylabel('Sales')
plt.title('Trends of Sales in Months and Years')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('./imgs/sales-months-years.png')
plt.show()

#calculate sales per month
monthly_sales = df.groupby('Order Month')['Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(monthly_sales['Order Month'], monthly_sales['Sales'])
plt.plot(monthly_sales['Order Month'], monthly_sales['Sales'], '-o', color='black')
plt.xlabel('Order Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.savefig('./imgs/monthly-sales.png')
plt.show()

#trends of profit in months and years
profit_months_years = df.groupby(['Order Year', 'Order Month'])['Profit'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(profit_months_years['Order Year'].astype(str) + '-' + profit_months_years['Order Month'].astype(str).str.zfill(2), profit_months_years['Profit'])
plt.plot(profit_months_years['Order Year'].astype(str) + '-' + profit_months_years['Order Month'].astype(str).str.zfill(2), profit_months_years['Profit'], '-o', color='black')
plt.xlabel('Year-Month')
plt.ylabel('Profit')
plt.title('Trends of Profit in Months and Years')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('./imgs/profit-months-years.png')
plt.show()

#calculate profit per month
monthly_profit = df.groupby('Order Month')['Profit'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(monthly_profit['Order Month'], monthly_profit['Profit'])
plt.plot(monthly_profit['Order Month'], monthly_profit['Profit'], '-o', color='black')
plt.xlabel('Order Month')
plt.ylabel('Profit')
plt.title('Monthly Proft')
plt.savefig('./imgs/monthly-profit.png')
plt.show()

#sales by category
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.pie(sales_by_category['Sales'], labels=sales_by_category['Category'], autopct='%1.1f%%')
plt.title('Sales by Category')
plt.axis('equal')
plt.tight_layout()
plt.savefig('./imgs/sales-by-category.png')
plt.show()

#profit by category
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.pie(profit_by_category['Profit'], labels=profit_by_category['Category'], autopct='%1.1f%%')
plt.title('Profit by Category')
plt.axis('equal')
plt.tight_layout()
plt.savefig('./imgs/profit-by-category.png')
plt.show()

#sales by sub-category
sales_by_sub_category = df.groupby('Sub-Category')['Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(sales_by_sub_category['Sub-Category'], sales_by_sub_category['Sales'])
plt.xlabel('Sub category')
plt.ylabel('Sales')
plt.title('Sales by Sub Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./imgs/sales-by-sub-category.png')
plt.show()

#profit by sub-category
profit_by_sub_category = df.groupby('Sub-Category')['Profit'].sum().reset_index()
plt.figure(figsize=(12, 6))

bars = plt.bar(profit_by_sub_category['Sub-Category'], profit_by_sub_category['Profit'])

for bar in bars:
    if bar.get_height() < 0:
        bar.set_color('red')

plt.xlabel('Sub category')
plt.ylabel('Profit')
plt.title('Profit by Sub Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./imgs/profit-by-sub-category.png')
plt.show()

#profit by product
profit_by_product = df.groupby('Product Name')['Profit'].sum().reset_index()
profit_by_product = profit_by_product.sort_values(by='Profit', ascending=False)
top_5_profit = profit_by_product.head(5)
bottom_5_profit = profit_by_product.tail(5)
combined_df = pd.concat([top_5_profit, bottom_5_profit])

plt.figure(figsize=(12, 6))
bars = plt.barh(combined_df['Product Name'], combined_df['Profit'])

for i, bar in enumerate(bars):
    if i >= len(top_5_profit):
        bar.set_color('red')

plt.xlabel('Product Name')
plt.ylabel('Profit')
plt.title('Top 5 and Bottom 5 profit by Product')

plt.tight_layout()
plt.savefig('./imgs/top-bottom-5-profit-product_name.png')
plt.show()

#comparison by region
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(sales_by_region['Region'], sales_by_region['Sales'])
plt.xlabel('Region')
plt.ylabel('Sales')
plt.title('Sales by Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./imgs/sales-by-region.png')
plt.show()

profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(profit_by_region['Region'], profit_by_region['Profit'])
plt.xlabel('Region')
plt.ylabel('Profit')
plt.title('Profit by Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./imgs/profit-by-region.png')
plt.show()

#Sales comparison by region in each year
regions = df['Region'].unique()
fig, ax = plt.subplots(figsize=(12, 8))

for region in regions:
    region_data = df[df['Region'] == region]
    sales_per_year = region_data.groupby('Order Year')['Sales'].sum().reset_index()
    ax.plot(sales_per_year['Order Year'], sales_per_year['Sales'], label=region)
plt.xlabel('Order Year')
plt.ylabel('Sales')
plt.title('Sales Over the Years')
plt.grid(True)
ax.legend(title='Region', loc='upper left')
plt.savefig('./imgs/sales-over-the-years.png')
plt.show()

#Profit comparison by region in each year
regions = df['Region'].unique()
fig, ax = plt.subplots(figsize=(12, 8))

for region in regions:
    region_data = df[df['Region'] == region]
    profit_per_year = region_data.groupby('Order Year')['Profit'].sum().reset_index()
    ax.plot(profit_per_year['Order Year'], profit_per_year['Profit'], label=region)
plt.xlabel('Order Year')
plt.ylabel('Profit')
plt.title('Profit Over the Years')
plt.grid(True)
ax.legend(title='Region', loc='upper left')
plt.savefig('./imgs/profit-over-the-years.png')
plt.show()

#profit by states
profit_by_states = df.groupby('State')['Profit'].sum().reset_index()
profit_by_states = profit_by_states.sort_values(by='Profit', ascending=False)
top_5_profit = profit_by_states.head(5)
bottom_5_profit = profit_by_states.tail(5)
combined_df = pd.concat([top_5_profit, bottom_5_profit])

plt.figure(figsize=(12, 6))
bars = plt.barh(combined_df['State'], combined_df['Profit'])

for i, bar in enumerate(bars):
    if i >= len(top_5_profit):
        bar.set_color('red')

plt.xlabel('States')
plt.ylabel('Profit')
plt.title('Top 5 and Bottom 5 profit by State')

plt.tight_layout()
plt.savefig('./imgs/top-bottom-5-profit-State.png')
plt.show()

# hypotesis df
least_30_profitable_products = df.nsmallest(30, 'Profit')
lowest_30_profit_margin = df.nsmallest(30, 'Profit Margin')

least_30_profitable_products_index = least_30_profitable_products.index.tolist()
lowest_30_profit_margin_index = lowest_30_profit_margin.index.tolist()

hypotesis_df = df.drop(least_30_profitable_products_index + lowest_30_profit_margin_index)

# comparison between the hypothesis
profit_per_year = df.groupby('Order Year')['Profit'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(profit_per_year['Order Year'], profit_per_year['Profit'], marker='o', linestyle='-')
plt.xlabel('Order Year')
plt.ylabel('Profit')
plt.title('Profit per Year')
plt.grid(True)
plt.savefig('./imgs/profit-per-year.png')
plt.show()

hypotesis_profit_per_year = hypotesis_df.groupby('Order Year')['Profit'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(hypotesis_profit_per_year['Order Year'], hypotesis_profit_per_year['Profit'], marker='o', linestyle='-')
plt.xlabel('Order Year')
plt.ylabel('Profit')
plt.title('Hypotesis Profit per Year')
plt.grid(True)
plt.savefig('./imgs/hypotesis-profit-per-year.png')
plt.show()