import speedtest
import time
import csv
from datetime import datetime


# Function to test the internet connection speed
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        results = st.results.dict()
        return results['download'] / 1000, results['upload'] / 1000  # Convert to Kb/s
    except (speedtest.SpeedtestBestServerFailure, speedtest.ConfigRetrievalError) as e:
        print(f"Error: {e}. Skipping this measurement.")
        return None, None


# Function to save results to a CSV file
def save_to_csv(timestamp, download, upload, filename='speedtest_results.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, download, upload])


# Function for in-place countdown
def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f'\rNext measurement in {remaining} seconds...', end='', flush=True)
        time.sleep(1)
    print('\rStarting measurement...            ')


# Main function of the program
def main():
    filename = 'speedtest_results.csv'

    # Create CSV file with headers if it doesn't exist
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Download (Kb/s)', 'Upload (Kb/s)'])

    try:
        while True:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            download, upload = test_speed()
            if download is not None and upload is not None:
                save_to_csv(timestamp, download, upload, filename)
                print(f'{timestamp} - Download: {download:.2f} Kb/s, Upload: {upload:.2f} Kb/s')
            countdown(30)  # Countdown for 0,5 minutes (30 seconds)
    except KeyboardInterrupt:
        print('Program terminated.')


if __name__ == "__main__":
    main()
