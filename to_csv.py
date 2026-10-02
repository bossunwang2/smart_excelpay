import argparse
import os

from data_process import CyclingDataProcessor


def round_paths(round_number):
    file_path = f"cycling_data_round{round_number}.txt"
    output_csv = f"cycling_data_round{round_number}.csv"
    return file_path, output_csv


def parse_round(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("round", type=int, help="round number to process, e.g. 9 for cycling_data_round9.txt")
    args = parser.parse_args()

    file_path, _ = round_paths(args.round)
    if not os.path.isfile(file_path):
        parser.error(f"{file_path} not found")
    return args.round


def process(file_path, output_csv):
    processor = CyclingDataProcessor(file_path, output_csv)
    df = processor.process()
    return df


if __name__ == '__main__':
    round_number = parse_round("Convert the cycling data of a round into a CSV file.")
    file_path, output_csv = round_paths(round_number)
    process(file_path, output_csv)
    print(f"{file_path} -> {output_csv}")
