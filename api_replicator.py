import requests
import json

# The URL we are sending the request to
url = "https://discord.com/api/v9/auth/login"

# The headers we will send to mimic the real Discord client.
# We copy these directly from the "Headers" tab in Fiddler.
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Placeholder",
    "X-Super-Properties": "Placeholder" # NOTE: It's best to copy the exact long string from your own Fiddler capture
}

# The data payload we are sending.
# This comes from the "JSON" tab in Fiddler.
payload = {
    "login": "Placeholder", # Replace with your email
    "password": "Placeholder",      # Replace with your password
    "undelete": False
}

# Send the POST request
print("Sending login request to Discord API...")
response = requests.post(url, headers=headers, json=payload)

# Print the server's response
print(f"Status Code: {response.status_code}")
print("Response Body:")
try:
    # Print the JSON response if possible
    print(json.dumps(response.json(), indent=2))
except json.JSONDecodeError:
    # Print as text if it's not JSON
    print(response.text)