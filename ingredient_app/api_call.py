import requests
import pprint

api_key = "81986bd69a244a718c5cd506c8bef528"

"""
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
"""
# Ingredient info

def ingredient_info(ingredient_id):
    url = f"https://api.spoonacular.com/food/ingredients/{ingredient_id}/information"
    endpoint = f"{url}?apiKey={api_key}"

    response = requests.get(endpoint, params={
        "amount": 1,
        "unit": "piece",
    })

    data = response.json()
    #pprint.pprint(data)

    result_list = []
    
    nutrition = data["nutrition"]
    
    image = data["image"]

    product_name = data["name"] 
    img_url = f"https://spoonacular.com/cdn/ingredients_250x250/{image}"
    amount = data["amount"]
    unit = data["unit"]
    carbs = nutrition["caloricBreakdown"]["percentCarbs"]
    fat = nutrition["caloricBreakdown"]["percentFat"]
    protein = nutrition["caloricBreakdown"]["percentProtein"]

    result_list.append(
        {
            "product_name": product_name,
            "img_url": img_url,
            "amount": amount,
            "unit": unit,
            "carbs": carbs,
            "fat": fat,
            "protein": protein,
        }
    )

    #print(product_name)
    #print(f"carbs: {carbs}, fat: {fat}, protein: {protein}")

    return result_list

#ingredient_info(9266)