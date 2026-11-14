// Run: npm install && APIFY_TOKEN=... node example.mjs
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
