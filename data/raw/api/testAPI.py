import requests as r

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
  