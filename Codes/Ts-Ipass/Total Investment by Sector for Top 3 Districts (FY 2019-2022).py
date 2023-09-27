import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('fact_TS_iPASS.csv')

# Convert the 'Starting_Date_Of_Month' column to a datetime format
df['Starting_Date_Of_Month'] = pd.to_datetime(df['Starting_Date_Of_Month'], format='%d-%b-%y')

# Filter data for FY 2019 to 2022
start_date = pd.Timestamp('2019-01-01')
end_date = pd.Timestamp('2022-12-31')
filtered_df = df[(df['Starting_Date_Of_Month'] >= start_date) & (df['Starting_Date_Of_Month'] <= end_date)]

# Group data by district and sector and calculate the total investment for each combination
district_sector_investment = filtered_df.groupby(['Dist_Name', 'Sector'])['Investment_In_Cr'].sum().reset_index()

# Find the top 3 districts with the highest total investments
top_districts = district_sector_investment.groupby('Dist_Name')['Investment_In_Cr'].sum().nlargest(3).index

# Filter data for the top 3 districts
top_district_data = district_sector_investment[district_sector_investment['Dist_Name'].isin(top_districts)]

# Create a bar chart to visualize the total investments by sector for the top 3 districts
plt.figure(figsize=(12, 6))
for district in top_districts:
    district_data = top_district_data[top_district_data['Dist_Name'] == district]
    plt.bar(district_data['Sector'], district_data['Investment_In_Cr'], label=district)

plt.xlabel('Sector')
plt.ylabel('Total Investment (in Crores)')
plt.title('Total Investment by Sector for Top 3 Districts (FY 2019-2022)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()

# Display the chart
plt.show()
