import requests
import sys

webhook_url = sys.argv[1]

f = open(sys.argv[2], "r")
code_snippet = f.read()
f.close()

# Construct the message payload
payload = {
    "text": "Output : ",
    "attachments": [
        {
            "text": "```" + code_snippet.strip() + "```",
            "mrkdwn_in": ["text"]
        }
    ]
}

# Send the message using the Slack webhook URL
response = requests.post(webhook_url, json=payload)

# Check the response status code
if response.status_code != 200:
    print("Failed to send message to Slack.")
