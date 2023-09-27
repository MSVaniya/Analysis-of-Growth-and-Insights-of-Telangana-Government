import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
df = pd.read_csv('fact_transport.csv')

# Calculate the vehicle sales growth for each district and fuel type
df['Total_Sales'] = df['fuel_type_petrol'] + df['fuel_type_diesel'] + df['Fuel_Type_Electric']

# Filter the data for FY 2022 and FY 2021
df_2022 = df[df['Starting_Date_Of_Month'].str.contains('22')]
df_2021 = df[df['Starting_Date_Of_Month'].str.contains('19')]

# Group the data by fuel type and district
groups_2022 = df_2022.groupby(['Dist_Name']).sum()
groups_2021 = df_2021.groupby(['Dist_Name']).sum()

# Calculate the percentage growth for each group
groups_2022['Growth'] = ((groups_2022['Total_Sales'] - groups_2021['Total_Sales']) / groups_2021['Total_Sales']) * 100

# Sort the groups by growth and select the top 3 and bottom 3 for each fuel type
top_bottom_districts = {}
fuel_types = ['fuel_type_petrol', 'fuel_type_diesel', 'Fuel_Type_Electric']

for fuel_type in fuel_types:
    sorted_df = groups_2022.sort_values(by='Growth', ascending=False)
    top_3 = sorted_df.head(3)
    bottom_3 = sorted_df.tail(3)
    top_bottom_districts[fuel_type] = {'Top 3': top_3, 'Bottom 3': bottom_3}

# Create bar charts to visualize the results
for fuel_type, data in top_bottom_districts.items():
    for category, df_category in data.items():
        df_category.plot(kind='bar', y='Growth', legend=False)
        plt.title(f'{category} Districts for {fuel_type}')
        plt.xlabel('District')
        plt.ylabel('Growth Percentage')
        plt.show()
