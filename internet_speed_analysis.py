import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'speedtest_results.csv'
speedtest_results = pd.read_csv(file_path)

# Convert the Timestamp column to datetime format
speedtest_results['Timestamp'] = pd.to_datetime(speedtest_results['Timestamp'])

# Set the Timestamp column as the index of the DataFrame
speedtest_results.set_index('Timestamp', inplace=True)

# Create a plot of download and upload speeds over time
plt.figure(figsize=(12, 6))
plt.plot(speedtest_results.index, speedtest_results['Download (Kb/s)'], label='Download (Kb/s)')
plt.plot(speedtest_results.index, speedtest_results['Upload (Kb/s)'], label='Upload (Kb/s)')
plt.xlabel('Timestamp')
plt.ylabel('Speed (Kb/s)')
plt.title('Internet Speed Test Results')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
