import os
import json
import requests
import base64
from keys import *


encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
        {"role": "user", "content": [
            {"type": "text", "text": "can you explain the image"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{encoded_image}"}
            }
        ]}
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 4096
}

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.json()['choices'][0]['message']['content'])