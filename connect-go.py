import requests
from datetime import datetime
import json
import os

today = datetime.now().strftime('%Y-%m-%d')

url = f"https://www.nytimes.com/svc/connections/v2/{today}.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    with open('connect.json', 'w') as f:
        json.dump(data, f)
    print("Successfully saved puzzle data!")
else:
    print(f"Failed to fetch. Status: {response.status_code}")
    exit(1)