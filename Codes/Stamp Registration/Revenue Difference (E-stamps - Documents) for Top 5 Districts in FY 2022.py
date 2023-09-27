import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('fact_stamps.csv')

# Assuming 'Starting_Date_Of_Month' column contains dates, parse them as datetime objects
df['Starting_Date_Of_Month'] = pd.to_datetime(df['Starting_Date_Of_Month'])

# Filter the data for FY 2022 (assuming FY starts from Jan 1, 2022, and ends on Dec 31, 2022)
fy_start = pd.to_datetime('2022-01-01')
fy_end = pd.to_datetime('2022-12-31')
df_fy_2022 = df[(df['Starting_Date_Of_Month'] >= fy_start) & (df['Starting_Date_Of_Month'] <= fy_end)]

# Calculate total revenue for document registration and e-stamp challans
total_document_revenue = df_fy_2022['Documents_Registered_Rev'].sum()
total_estamps_revenue = df_fy_2022['Estamps_Challans_Rev'].sum()

# Calculate the revenue difference
revenue_difference = total_estamps_revenue - total_document_revenue

# Identify the top 5 districts where e-stamps revenue exceeds document revenue the most
top_5_districts = df_fy_2022.groupby('Dist_Name')['Estamps_Challans_Rev', 'Documents_Registered_Rev'].sum()
top_5_districts['Revenue_Difference'] = top_5_districts['Estamps_Challans_Rev'] - top_5_districts['Documents_Registered_Rev']
top_5_districts = top_5_districts.sort_values(by='Revenue_Difference', ascending=False).head(5)

# Create a bar chart to visualize the revenue difference for the top 5 districts
plt.figure(figsize=(10, 6))
top_5_districts['Revenue_Difference'].plot(kind='bar', color='skyblue')
plt.title('Revenue Difference (E-stamps - Documents) for Top 5 Districts in FY 2022')
plt.xlabel('District')
plt.ylabel('Revenue Difference')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Display the total revenue and revenue difference
print(f"Total Document Registration Revenue in FY 2022: {total_document_revenue}")
print(f"Total E-stamps Challans Revenue in FY 2022: {total_estamps_revenue}")
print(f"Revenue Difference (E-stamps - Documents) in FY 2022: {revenue_difference}")
