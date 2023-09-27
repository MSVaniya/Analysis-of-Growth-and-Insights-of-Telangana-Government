import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('fact_TS_iPASS.csv')

# Convert the 'Starting Date Of Month' column to datetime
df['Starting_Date_Of_Month'] = pd.to_datetime(df['Starting_Date_Of_Month'], format='%d-%b-%y')

# Filter data for FY 2022 (assuming FY 2022 starts from April 2021 and ends in March 2022)
fy_start = pd.to_datetime('2022-01-01')
fy_end = pd.to_datetime('2022-12-31')
fy_data = df[(df['Starting_Date_Of_Month'] >= fy_start) & (df['Starting_Date_Of_Month'] <= fy_end)]

# Group data by 'Sector' and sum the 'Investment In Cr' for each sector
sector_investment = fy_data.groupby('Sector')['Investment_In_Cr'].sum().reset_index()

# Sort sectors by investment amount in descending order
top_sectors = sector_investment.sort_values(by='Investment_In_Cr', ascending=False).head(5)

# Plot the top sectors using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_sectors['Sector'], top_sectors['Investment_In_Cr'])
plt.xlabel('Sector')
plt.ylabel('Total Investment (in Crores)')
plt.title('Top 5 Sectors with the Most Investment in FY 2022')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Display the top sectors and their total investments
print(top_sectors)
