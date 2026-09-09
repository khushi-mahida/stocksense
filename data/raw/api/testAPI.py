'''import requests as r

url = "https://dummyjson.com/products"
response=r.get(url)
print("status code:",response.status_code)
data = response.json()
print (data)
## this is to see if i can import the data from the api 
# and print it in the console.
## now we  will clean this  messy data its is more messy than my life  that saying a lot 
#about the  data not me 
products = data['products']
for product in products[:5]:  # Print details of the first 5 products
    print("Product ID:", product['id'])
    print("Title:", product['title'])
    print("Description:", product['description'])
    print("Price:", product['price'])
    print("Brand:", product['brand'])
    print("Category:", product['category'])
    print("Rating:", product['rating'])
    print("Stock:", product['stock'])
    print("Thumbnail URL:", product['thumbnail'])
    print("Images URLs:", product['images'])
  '''
  #/resource/9ef84268-d588-465a-a308-a864a43d0070
  # sabji mandi ap reults 
import requests

API_KEY = "579b464db66ec23bdd000001df2fb96816b3407b6b599072df27fd6d"
RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"
import requests


url = f"https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"

params = {
    "api-key": API_KEY,
    "format": "json",
    "limit": 10
}

response = requests.get(url, params=params)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("content-type"))
print("URL:", response.url)
print("Response:")
print(response.text[:2000])



