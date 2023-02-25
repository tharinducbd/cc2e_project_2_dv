import json

from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

# Explore the structure of the data.
filename = 'cc2e_codes/project_2/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# # Make readable output (temporary) to see the data structure
# readable_file = 'cc2e_codes/project_2/data/eq_readable_1d_m1.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

# Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
