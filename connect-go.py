import requests
from datetime import datetime
import json
import os

today = datetime.now().strftime('%Y-%m-%d')
url = f"https://nytimes.com{today}.json"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    os.makedirs('data', exist_ok=True)
    with open(f'data/connections.json', 'w') as f:
        json.dump(data, f)