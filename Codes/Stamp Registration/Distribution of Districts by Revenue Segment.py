import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('fact_stamps.csv')

# Assuming the date column is named 'Starting_Date_Of_Month,' convert it to datetime
df['Starting_Date_Of_Month'] = pd.to_datetime(df['Starting_Date_Of_Month'])

# Filter data for the fiscal year 2021-2022
start_date = pd.to_datetime('2021-04-01')  # Start of fiscal year
end_date = pd.to_datetime('2022-03-31')    # End of fiscal year
fiscal_year_data = df[(df['Starting_Date_Of_Month'] >= start_date) & (df['Starting_Date_Of_Month'] <= end_date)]

# Group the data by district and sum the revenue
district_revenue = fiscal_year_data.groupby('Dist_Name')['Documents_Registered_Rev'].sum().reset_index()

# Calculate percentiles to determine segments
percentiles = district_revenue['Documents_Registered_Rev'].quantile([0, 0.33, 0.67, 1])

# Create a function to assign segments based on revenue
def categorize_segment(revenue):
    if revenue <= percentiles[0.33]:
        return 'Low Revenue'
    elif revenue <= percentiles[0.67]:
        return 'Medium Revenue'
    else:
        return 'High Revenue'

# Apply the function to categorize districts
district_revenue['Revenue_Segment'] = district_revenue['Documents_Registered_Rev'].apply(categorize_segment)

# Count the districts in each segment
segment_counts = district_revenue['Revenue_Segment'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(segment_counts.index, segment_counts.values)
plt.xlabel('Revenue Segment')
plt.ylabel('Number of Districts')
plt.title('Distribution of Districts by Revenue Segment')
plt.show()
