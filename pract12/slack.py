import requests


token = "xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77"
message = "goose"
url = "https://slack.com/api/chat.postMessage"
channel_id = "C090QB0L230"
headers = {"Authorization": f"Bearer {token}",
    "Content-Type": "application/json"}
data = {    "channel": channel_id,
    "text": message}
res = requests.post(url, headers=headers, json=data)
print(requests.json)