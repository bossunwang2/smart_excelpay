from data_process import CyclingDataProcessor


def process(file_path, output_csv):
    processor = CyclingDataProcessor(file_path, output_csv)
    df = processor.process()
    return df


if __name__ == '__main__':
    file_path = "cycling_data_round5.txt"
    output_csv = "cycling_data_round5.csv"
    process(file_path, output_csv)
