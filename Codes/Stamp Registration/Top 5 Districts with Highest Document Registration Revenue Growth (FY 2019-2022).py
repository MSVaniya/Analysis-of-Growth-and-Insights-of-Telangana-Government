import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('fact_stamps.csv')

# Convert the 'Starting_Date_Of_Month' column to datetime format
df['Starting_Date_Of_Month'] = pd.to_datetime(df['Starting_Date_Of_Month'])

# Filter data for FY 2019 and FY 2022
start_date_2019 = pd.Timestamp('2019-01-01')  # Assuming the fiscal year starts in April
end_date_2019 = pd.Timestamp('2019-12-31')
start_date_2022 = pd.Timestamp('2022-01-01')
end_date_2022 = pd.Timestamp('2022-12-31')

df_2019 = df[(df['Starting_Date_Of_Month'] >= start_date_2019) & (df['Starting_Date_Of_Month'] <= end_date_2019)]
df_2022 = df[(df['Starting_Date_Of_Month'] >= start_date_2022) & (df['Starting_Date_Of_Month'] <= end_date_2022)]

# Group data by district and calculate the total revenue for each year
revenue_2019 = df_2019.groupby('Dist_Name')['Documents_Registered_Rev'].sum()
revenue_2022 = df_2022.groupby('Dist_Name')['Documents_Registered_Rev'].sum()

# Calculate revenue growth for each district
revenue_growth = (revenue_2022 - revenue_2019) / revenue_2019 * 100

# Sort districts by revenue growth in descending order and get the top 5
top_5_growth_districts = revenue_growth.sort_values(ascending=False).head(5)

# Plot the revenue growth for the top 5 districts
plt.figure(figsize=(12, 6))
top_5_growth_districts.plot(kind='bar', color='skyblue')
plt.title('Top 5 Districts with Highest Document Registration Revenue Growth (FY 2019-2022)')
plt.xlabel('District')
plt.ylabel('Revenue Growth (%)')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Print the top 5 districts with their revenue growth
print("Top 5 Districts with Highest Document Registration Revenue Growth (FY 2019-2022):\n")
print(top_5_growth_districts)

# Optionally, you can save the plot to a file
# plt.savefig('revenue_growth_top_5_districts.png')

# Optionally, you can also save the top 5 districts to a CSV file
# top_5_growth_districts.to_csv('top_5_growth_districts.csv')
