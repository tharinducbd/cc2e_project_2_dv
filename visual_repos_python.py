import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = ('https://api.github.com/search/repositories?'
       'q=language:python&sort=stars')
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# Process Results
response_dict = r.json()
repo_dict = response_dict['items']

