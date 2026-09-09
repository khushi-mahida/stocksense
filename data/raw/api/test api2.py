import requests

API_KEY = "579b464db66ec23bdd0000017fdfcb64c10e462c60dfca466bd74938"
RESOURCE_ID = "35985678-0d79-46b4-9ed6-6f13308a1d24"
url = f"https://api.data.gov.in/resource/35985678-0d79-46b4-9ed6-6f13308a1d24"

if not API_KEY or API_KEY.startswith("YOUR"):
    print("API key is missing or still a placeholder.")
    print("Replace YOUR_NEW_API_KEY with your real data.gov.in API key and run the script again.")
    raise SystemExit(1)

params = {
    "api-key": API_KEY,
    "format": "json",
    "limit": 10,
}

try:
    response = requests.get(url, params=params, timeout=500)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Request timed out while waiting for the API.")
    print("Check your internet connection, API status, or increase the timeout value.")
    raise SystemExit(1)
except requests.exceptions.RequestException as exc:
    print("API request failed:")
    print(exc)
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
    
    
    
    
    