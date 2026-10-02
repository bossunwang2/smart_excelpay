# Cycling Data Processor

## Description
This script reads a text file containing cycling data, processes it, and outputs a structured CSV file. It organizes the data with participant IDs as rows and dates as columns, with a `Total` column for each participant and an `Overall Total` row for each date.

## Quick Start
> **Generating the CSV is the main thing this repo is used for.** Add the records of the round to `cycling_data_round<N>.txt`, then run:
>
> ```sh
> python to_csv.py <round>
> ```
>
> e.g. `python to_csv.py 9` reads `cycling_data_round9.txt` and writes `cycling_data_round9.csv`.

## Requirements
- Python 3.x
- pandas library
- flask library (only for the optional query service)

## Installation
1. Ensure you have Python installed.
2. Install the required library if not already installed:
   ```sh
   pip install pandas flask
   ```

## Usage

### Generate the CSV (main workflow)
1. Prepare a text file for the round (`cycling_data_round<N>.txt`, e.g. `cycling_data_round9.txt`) with data in the following format:
   ```
   YYYY_MM_DD,Name1/Name2/Name3,Value
   ```
   Example:
   ```
   2025_01_21,Arthur/Bossun/JJ/Rex/Chaihung,245
   ```
2. Run the script with the round number to process:
   ```sh
   python to_csv.py <round>
   ```
   Example, for round 9:
   ```sh
   python to_csv.py 9
   ```
3. The processed data will be saved in `cycling_data_round<N>.csv` (e.g. `cycling_data_round9.csv`). The CSV files are generated output and are not committed.

The round number is required; run `python to_csv.py -h` to see the usage. An unknown round (no matching `cycling_data_round<N>.txt`) exits with an error.

### Query service (optional, rarely used)
1. Run the script for service with the round number to serve (this also regenerates the CSV of that round):
   ```sh
   python service.py <round>
   ```
   Example, for round 9:
   ```sh
   python service.py 9
   ```
2. copy URL to query personal data:
   #### Example:
   - enter URL
   ```
   http://192.168.10.59:9487/query?ID=JJ
   ```
   - output on webpage:
   ```
   {"2025_01_21":245,"total":245}
   ```

## Output
- The CSV file will contain:
  - Participants as rows
  - A `Total` column summing up the values for each participant, followed by one column per date
  - A final row labeled `Overall Total` summing up the values of all participants

## Example Output CSV:
```
,Total,2025_01_21,2025_01_28
Arthur,490.0,245.0,245.0
Bossun,490.0,245.0,245.0
JJ,245.0,245.0,
Overall Total,1225.0,735.0,490.0
```

## Notes
- Ensure the text file follows the specified format.
- Modify the script to handle different data structures if needed.
