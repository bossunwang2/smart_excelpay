import pandas as pd
from flask import Flask
from flask import jsonify
from flask import request

from to_csv import process

app = Flask(__name__)
# Enable pretty-printing of JSON in Flask
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Load the CSV file into a DataFrame
file_path = "cycling_data_round1.txt"
output_csv = "cycling_data_round1.csv"
process(file_path, output_csv)
df = pd.read_csv(output_csv)
df = df.astype('object')

# Endpoint to get all records
@app.route('/records', methods=['GET'])
def get_all_records():
    return jsonify(df.to_dict())

# Endpoint to query records based on an ID column
@app.route('/query', methods=['GET'])
def query_records():
    column = request.args.get('ID')  # ID column to query
    if column and column in df.columns:
        # Get the date and total values for the specified ID column
        date_dict = {df.iloc[idx, 0]: df.iloc[idx][column] for idx in range(df.shape[0] - 1)}

        # Get the "Total" row to use for totals
        total_row = df.iloc[-1]  # Assuming "Total" row is always second
        total_dict = {
            "total": total_row[column]  # Corresponding total value for the ID
        }

        combined_dict = {**date_dict, **total_dict}

        return jsonify(combined_dict)
    else:
        return jsonify({'error': 'Invalid column parameter'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9487)
