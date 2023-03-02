import requests

# Make an API call and store the response.
url = ('https://api.github.com/search/repositories?'
       'q=language:python&sort=stars')

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()

# Process results.
print(response_dict.keys())
print(f"Total Repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}")

# Examine the firts repo.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
