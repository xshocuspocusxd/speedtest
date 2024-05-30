# Internet Speed Analysis

## Description
This repository contains two scripts for measuring and analyzing internet speed:

1. **speedtest_collector.py**: Continuously measures the internet connection speed (download and upload) and saves the results in a CSV file.
2. **internet_speed_analysis.py**: Analyzes the results saved in the CSV file and generates a plot of download and upload speeds over time.

## Requirements
- Python 3.x
- pandas
- matplotlib
- speedtest-cli

## Setup
1. Install the required packages using pip:
    ```bash
    pip install pandas matplotlib speedtest-cli
    ```

2. Clone this repository or download the scripts.

## Usage

### speedtest_collector.py
This script measures the internet speed at regular intervals and saves the results to a CSV file.

#### How to Run
1. Ensure you have the required packages installed.
2. Run the script:
    ```bash
    python speedtest_collector.py
    ```
