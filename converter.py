from copy import deepcopy
import glob
import json
import os
import sys
import pandas


def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem


def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for item in data:
                [rows.append(elem) for elem in flatten_list(flatten_json(item, prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))


if __name__ == '__main__':
    try:
        merge_csv = eval(sys.argv[1].title())
    except Exception as e:
        merge_csv = False
    print(f"Merging all data in a single CSV file? '{merge_csv}'.")
    try:
        data_folder = sys.argv[2]
    except Exception as e:
        data_folder = 'data'
    print(f"Using input data folder '{data_folder}'.")

    try:
        os.mkdir('output')
        print(f"Created directory 'output' where the CSV files are saved.")
    except FileExistsError:
        print(f"Directory 'output' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create 'output'.")
    except Exception as e:
        print(f"An error occurred: {e}.")

    merged_df = pandas.DataFrame()
    all_files = glob.glob(data_folder + "/*.json")
    for filepath in all_files:
        file = os.path.splitext(os.path.basename(filepath))[0]
        with open(filepath, encoding='utf-8') as inputfile:
            data = json.loads(inputfile.read())
        df = json_to_dataframe(data)
        print(f"Flattened JSON '{filepath}'.")
        if merge_csv:
            merged_df = pandas.concat([merged_df, df], sort = False, ignore_index = True)
        else:
            df.to_csv('output/' + file + '.csv', index=False, sep=';')
            print(f"Saved JSON to CSV 'output/{file}.csv'.")

if merge_csv:
    merged_df.to_csv('output/all_merged.csv', index=False, sep=';')
    print(f"Saved all JSON to single CSV 'output/all_merged.csv'.")
