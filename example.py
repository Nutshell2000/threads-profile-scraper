# Run: pip install apify-client && APIFY_TOKEN=... python example.py
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "usernames": [
        "nba",
        "https://www.threads.com/@nasa"
    ]
}

run = client.actor("spellzcode/threads-profile-data").call(run_input=run_input)
for p in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(p.get('username'), p.get('followers'), (p.get('recentPosts') or [{}])[0].get('text'))
