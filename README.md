# System Usage Data Collector

The **System Usage Data Collector** is a Python script that collects and stores information about your system's CPU and memory (RAM) usage over a specified duration. It creates an Excel workbook with the collected data.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- The `psutil` and `xlsxwriter` Python packages. You can install them using `pip`:
  ```bash
  pip install psutil xlsxwriter

## Usage
1.Clone this repository to your local machine or download the system_usage_data_collector.py file.

2.Open a terminal or command prompt.

3.Navigate to the directory where the script is located.

4.Run the script by entering the following command:
```bash
python cpu_mem.py
```

5.The script will prompt you for the following inputs:

a.The name for the Excel file to be generated.
b.The duration (in minutes) for which you want to collect data.

6.The script will then collect data on CPU and memory usage for the specified duration with 10-second intervals.

7Once the data collection is complete, an Excel workbook named workbook_name.xlsx will be created in the same folder as the script.
  
## File Structure
The repository contains the following files and folders:

cpu_mem.py: The Python script for collecting and storing system usage data.

README.md: This README file.
