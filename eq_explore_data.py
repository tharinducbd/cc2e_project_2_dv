import json

# Explore the structure of the data.
filename = 'cc2e_codes/project_2/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'cc2e_codes/project_2/data/eq_readable_1d_m1.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
