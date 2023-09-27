import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
data = pd.read_csv('fact_TS_iPASS.csv') 

# Convert the 'Starting_Date_Of_Month' column to datetime
data['Starting_Date_Of_Month'] = pd.to_datetime(data['Starting_Date_Of_Month'])

# Filter data for FY 2021 and 2022
start_date_2021 = pd.to_datetime('2021-01-01')
end_date_2022 = pd.to_datetime('2022-12-31')
filtered_data = data[(data['Starting_Date_Of_Month'] >= start_date_2021) & (data['Starting_Date_Of_Month'] <= end_date_2022)]

# Group data by 'Sector' and 'Dist_Name' and calculate the total investment
investment_by_sector = filtered_data.groupby(['Sector', 'Dist_Name'])['Investment_In_Cr'].sum().reset_index()

# Identify sectors with substantial investments in multiple districts
substantial_investment = investment_by_sector.groupby('Sector')['Investment_In_Cr'].sum().reset_index()
substantial_investment = substantial_investment[substantial_investment['Investment_In_Cr'] > 50]  # Define your threshold

# Create a bar chart to visualize sectors with substantial investments
plt.figure(figsize=(12, 6))
sns.barplot(data=substantial_investment, x='Investment_In_Cr', y='Sector', palette='viridis')
plt.xlabel('Total Investment (in Crores)')
plt.ylabel('Sector')
plt.title('Sectors with Substantial Investments in Multiple Districts (FY 2021-2022)')
plt.show()
