# Threads Profile Scraper: followers, bio and recent posts

Get follower count, bio, verified status and recent posts for a list of Threads (threads.com) usernames or profile links. No login needed.

This repo is a working example of calling the [Threads Profile Scraper](https://apify.com/spellzcode/threads-profile-data) Apify actor from Node.js, Python, or without code. The actor runs on Apify's cloud; you pay per result and Apify's free plan includes $5 of monthly credit.

Made by SpellzCode, who also run the actor. Not affiliated with any site named here.

## What people use it for

- Track brand and competitor accounts on Threads
- Vet creators before a campaign
- Collect recent posts for monitoring

## Quick start without code

1. Open **[the actor on Apify](https://apify.com/spellzcode/threads-profile-data)** and sign in (free).
2. Paste your inputs, press **Start**.
3. Download the results as CSV, Excel or JSON, or connect them to Google Sheets, Make, Zapier or n8n.

## Quick start with code

Get an API token at [console.apify.com/settings/integrations](https://console.apify.com/settings/integrations), then:

```bash
git clone https://github.com/Nutshell2000/threads-profile-scraper.git
cd threads-profile-scraper
npm install
APIFY_TOKEN=your_token node example.mjs
```

Node.js ([example.mjs](example.mjs)):

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const input = {
  "usernames": [
    "nba",
    "https://www.threads.com/@nasa"
  ]
};

const run = await client.actor('spellzcode/threads-profile-data').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const p of items) console.log(p.username, p.followers, p.recentPosts?.[0]?.text ?? '');
```

Python ([example.py](example.py)):

```python
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
```

## Input

```json
{
  "usernames": [
    "nba",
    "https://www.threads.com/@nasa"
  ]
}
```

All fields are described on the actor's **Input** tab.

## Output (one row)

```json
{
  "query": "nba",
  "status": "ok",
  "username": "nba",
  "name": "NBA",
  "followers": 12186520,
  "verified": false,
  "bio": "The 2026-27 NBA season continues Saturday! NBA Mexico City Game 2026 🏀 5pm/et on NBA TV: Nuggets/Pacers",
  "avatarUrl": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/884852944_17998507866100489_481444679695143757_n.jpg",
  "postsReturned": 4,
  "recentPosts": [
    {
      "text": "NEW STANDINGS UPDATE 👀\n\nFor More ➡️ https://nba.smart.link/urt2hjrq0",
      "likes": null,
      "postedAt": null,
      "url": "https://www.threads.com/@nba/post/Dfbt3_dh7fv"
    }
  ],
  "url": "https://www.threads.com/@nba"
}
```

## Price

$3 per 1,000 profiles returned; missing accounts are free. Apify's paid plans get 10% to 30% off. Each run also has Apify's standard $0.00005 start charge.

## Limits

- Reads what Threads shows logged-out visitors, so likes and dates on recent posts can be empty.

## More tools

[All SpellzCode Apify actors](https://github.com/Nutshell2000/spellzcode-apify-actors): LinkedIn, TikTok and Threads profiles, company registers, contact details, email cleaning, PDFs, jobs, reviews and SEO.

## License

The example code in this repo is MIT licensed.
