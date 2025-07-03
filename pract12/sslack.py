from slack_sdk import WebClient

client = WebClient(token="xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77")
client.chat_postMessage(channel="C090QB0L230", blocks=[{"type":"image","image_url":"https://i.etsystatic.com/32429025/r/il/5eb357/3614210544/il_570xN.3614210544_leur.jpg", "alt_text":"goose"}])


