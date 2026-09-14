import time

import requests

API_KEY = "579b464db66ec23bdd000001df2fb96816b3407b6b599072df27fd6d"
RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"
url = f"https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"


if not API_KEY or API_KEY.startswith("YOUR"):
    print("API key is missing or still a placeholder.")
    print("Replace YOUR_NEW_API_KEY with your real data.gov.in API key and run the script again.")
    raise SystemExit(1)

params = {
    "api-key": API_KEY,
    "format": "json",
    "limit": 10,
}

for attempt in range(3):
    try:
        response = requests.get(url, params=params, timeout=7000)
        if response.status_code != 502:
            response.raise_for_status()
            break
        if attempt < 2:
            time.sleep(2 ** attempt)
    except requests.exceptions.Timeout:
        print("Request timed out while waiting for the API.")
        print("Check your internet connection, API status, or increase the timeout value.")
        raise SystemExit(1)
    except requests.exceptions.RequestException as exc:
        print("API request failed:")
        print(exc)
        raise SystemExit(1)
else:
    print("The data.gov.in gateway returned HTTP 502 after 3 attempts.")
    print(response.text[:2000])
    raise SystemExit(1)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("content-type"))
print("URL:", response.url)

try:
    data = response.json()
except ValueError:
    print("The API did not return valid JSON.")
    print(response.text[:2000])
    raise SystemExit(1)

print("\nData received:")
print(data)

records = data.get("records", [])
print("\nNumber of records:", len(records))

for record in records[:5]:
    print(record)
    
    
    
    
    