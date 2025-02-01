# Cycling Data Processor

## Description
This script reads a text file containing cycling data, processes it, and outputs a structured CSV file. It organizes the data with dates as row indices and participant IDs as columns. A final row is added to calculate the total values for each participant.

## Requirements
- Python 3.x
- pandas library

## Installation
1. Ensure you have Python installed.
2. Install the required library if not already installed:
   ```sh
   pip install pandas
   ```

## Usage
1. Prepare a text file (`cycling_data.txt`) with data in the following format:
   ```
   YYYY_MM_DD,Name1/Name2/Name3,Value
   ```
   Example:
   ```
   2025_01_21,Arthur/Bossun/JJ/Rex/Chaihung,245
   ```
2. Run the script:
   ```sh
   python to_csv.py
   ```
3. The processed data will be saved in `cycling_data.csv`.

## Output
- The CSV file will contain:
  - Dates as row indices
  - Participants as column headers
  - A final row labeled `Total` summing up the values for each participant

## Example Output CSV:
```
Date,Arthur,Bossun,JJ,Rex,Chaihung
2025_01_21,245,245,245,245,245
Total,245,245,245,245,245
```

## Notes
- Ensure the text file follows the specified format.
- Modify the script to handle different data structures if needed.

