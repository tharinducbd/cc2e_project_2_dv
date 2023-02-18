import csv

filename = 'cc2e_codes/project_2/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get high temperatures from the file.
    highs = [int(row[5]) for row in reader]

print(highs)

