import requests
import pprint

api_key = "81986bd69a244a718c5cd506c8bef528"

# Ingredient search
url = "https://api.spoonacular.com/food/ingredients/search"
endpoint = f"{url}?apiKey={api_key}"

response = requests.get(endpoint, params={
    "query": "egg",
    "number": "5"
})

data = response.json()
#pprint.pprint(data)

results = data["results"]

product_list = []
for result in results:
    product_id = result["id"]
    product_name = result["name"]
    #print(f"{product_id} - {product_name}")

    product_list.append({
        "id": product_id,
        "name": product_name,
    })

print(product_list)
print()

# Ingredient info

ingredient_id = int(product_list[0]["id"])
url = f"https://api.spoonacular.com/food/ingredients/{ingredient_id}/information"
endpoint = f"{url}?apiKey={api_key}"

response = requests.get(endpoint, params={
    "amount": 1,
    "unit": "piece",
})

#pprint.pprint(response.headers)
data = response.json()
#pprint.pprint(data)