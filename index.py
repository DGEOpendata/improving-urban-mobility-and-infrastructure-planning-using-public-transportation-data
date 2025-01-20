python
import pandas as pd
import matplotlib.pyplot as plt

# Load the public transportation dataset
data = pd.read_excel('Public_Transport_Usage_Abu_Dhabi.xlsx')

# Display the first few rows of the dataset
data.head()

# Analyze peak usage times
peak_times = data.groupby('Time_of_Day')['Ridership'].sum()

# Plot the peak usage times
def plot_peak_usage(peak_times):
    plt.figure(figsize=(10, 6))
    plt.plot(peak_times.index, peak_times.values, marker='o')
    plt.title('Peak Public Transportation Usage Times')
    plt.xlabel('Time of Day')
    plt.ylabel('Number of Riders')
    plt.grid(True)
    plt.show()

plot_peak_usage(peak_times)

# Analyze most popular routes
popular_routes = data.groupby('Route')['Ridership'].sum().nlargest(5)

# Plot the most popular routes
def plot_popular_routes(popular_routes):
    plt.figure(figsize=(12, 8))
    popular_routes.plot(kind='bar', color='skyblue')
    plt.title('Top 5 Most Popular Routes')
    plt.xlabel('Route')
    plt.ylabel('Total Ridership')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

plot_popular_routes(popular_routes)
