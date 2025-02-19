import pandas as pd


class CyclingDataProcessor:
    def __init__(self, file_path, output_csv):
        self.file_path = file_path
        self.output_csv = output_csv
        self.data_frames = []

    def read_file(self):
        with open(self.file_path) as file:
            lines = file.readlines()
        return lines

    def process_lines(self, lines):
        for line in lines:
            line = line.strip()
            if not line:
                continue

            date_str, ids_str, value = line.split(',')
            value = int(value)
            ids = ids_str.split('/')
            df = pd.DataFrame({id_: [value] for id_ in ids}, index=[date_str])
            self.data_frames.append(df)

    def save_to_csv(self):
        final_df = pd.concat(self.data_frames)

        # Fill missing values with 0 before summing
        # final_df = final_df.fillna(0)

        # Add a row to calculate total value for each participant
        total_row = final_df.sum(numeric_only=True).to_frame().T
        total_row.index = ["Total"]
        final_df = pd.concat([total_row, final_df])

        # Add a new row to summarize the overall total of all participants
        final_df["Overall Total"] = final_df.sum(axis=1)

        # Transform rows to columns
        final_df = final_df.transpose()

        final_df.to_csv(self.output_csv)
        return final_df

    def process(self):
        lines = self.read_file()
        self.process_lines(lines)
        return self.save_to_csv()