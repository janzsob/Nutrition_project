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

""" Ingredient info """
def ingredient_info(ingredient_id):
    url = f"https://api.spoonacular.com/food/ingredients/{ingredient_id}/information"
    endpoint = f"{url}?apiKey={api_key}"
    response = requests.get(endpoint, params={
        "amount": 1,
        "unit": "piece",
    })
    
    if response.status_code == 402: # in case of 402 error (when the number of requests reach the daily maximum limit)
        return "402 error"
    else:
        try: # The ideal way
            data = response.json()
            
            nutrition = data["nutrition"]
            image = data["image"]
            
            keys_list = [] # the generated lists will be stored here
            
            # main info
            main_info = []

            product_name = data["name"] 
            img_url = f"https://spoonacular.com/cdn/ingredients_250x250/{image}"
            product_amount = data["amount"]
            product_unit = data["unit"]
            carbs = nutrition["caloricBreakdown"]["percentCarbs"]
            fat = nutrition["caloricBreakdown"]["percentFat"]
            protein = nutrition["caloricBreakdown"]["percentProtein"]
            weight_amount = nutrition["weightPerServing"]["amount"]
            weight_unit = nutrition["weightPerServing"]["unit"]

            # category
            try:
                product_category = data["categoryPath"][0]
            except(IndexError):
                product_category = False

            main_info.append(
                {
                    "product_name": product_name,
                    "img_url": img_url,
                    "product_amount": product_amount,
                    "product_unit": product_unit,
                    "carbs": carbs,
                    "fat": fat,
                    "protein": protein,
                    "weight_amount": weight_amount,
                    "weight_unit": weight_unit,
                    "product_category": product_category,
                }
            )

            # all nutrients
            nutrients_list = []
            for nutrient in nutrition["nutrients"]:
                nutri_name = nutrient["name"]
                nutri_amount = nutrient["amount"]
                nutri_unit = nutrient["unit"]
                
                nutrients_list.append(
                    {
                        "nutri_name": nutri_name,
                        "nutri_amount": nutri_amount,
                        "nutri_unit": nutri_unit,
                    }
                )

            # removing main nutrients
            
            for num in range(len(nutrients_list)):
                if nutrients_list[num]["nutri_name"] == "Calories":
                    del nutrients_list[num]
                    break
                
            for num in range(len(nutrients_list)):
                if nutrients_list[num]["nutri_name"] == "Carbohydrates":
                    del nutrients_list[num]
                    break

            for num in range(len(nutrients_list)):
                if nutrients_list[num]["nutri_name"] == "Protein":
                    del nutrients_list[num]
                    break

            for num in range(len(nutrients_list)):
                if nutrients_list[num]["nutri_name"] == "Fat":
                    del nutrients_list[num]
                    break

            # main_nutrients
            calories_data =[]
            carbs_data = []
            protein_data = []
            fat_data = []

            for main_nutri in data["nutrition"]["nutrients"]:
                if main_nutri["name"] == "Calories":
                    calories_name = main_nutri["name"]
                    calories_amount = main_nutri["amount"]
                    calories_unit = main_nutri["unit"]

                    calories_data.append(
                        {
                        "calories_name": calories_name,
                        "calories_amount": calories_amount,
                        "calories_unit": calories_unit,
                        }
                    )

                if main_nutri["name"] == "Carbohydrates":
                    carbs_name = main_nutri["name"]
                    carbs_amount = main_nutri["amount"]
                    carbs_unit = main_nutri["unit"]

                    carbs_data.append(
                        {
                        "carbs_name": carbs_name,
                        "carbs_amount": carbs_amount,
                        "carbs_unit": carbs_unit,
                        }
                    )

                if main_nutri["name"] == "Protein":
                    protein_name = main_nutri["name"]
                    protein_amount = main_nutri["amount"]
                    protein_unit = main_nutri["unit"]

                    protein_data.append(
                        {
                        "protein_name": protein_name,
                        "protein_amount": protein_amount,
                        "protein_unit": protein_unit,
                        }
                    )

                if main_nutri["name"] == "Fat":
                    fat_name = main_nutri["name"]
                    fat_amount = main_nutri["amount"]
                    fat_unit = main_nutri["unit"]

                    fat_data.append(
                        {
                        "fat_name": fat_name,
                        "fat_amount": fat_amount,
                        "fat_unit": fat_unit,
                        }
                    )


            # glycemic
            glycemic_list = []
            for glycemic in nutrition["properties"]:
                glycemic_name = glycemic["name"]
                glycemic_amount = glycemic["amount"]

                glycemic_list.append(
                    {
                        "glycemic_name": glycemic_name,
                        "glycemic_amount": glycemic_amount,
                    }
                )

            keys_list.append( # addig the created list elements
                {
                    "main_info": main_info,
                    "nutrients_list": nutrients_list,
                    "glycemic_list": glycemic_list,
                    "calories_data": calories_data,
                    "carbs_data": carbs_data,
                    "protein_data": protein_data,
                    "fat_data": fat_data,

                }
            )

            return keys_list

        except(KeyError): # in case of KeyError, when the the given product id doesn't exists
            return KeyError

#pprint.pprint(ingredient_info(9037)[0]["calories_name"])
#pprint.pprint(ingredient_info(9037))




"""
list = [
    {'nutri_amount': 52.66, 'nutri_name': 'Carbohydrates', 'nutri_unit': 'g'},
    {'nutri_amount': 0.55, 'nutri_name': 'Vitamin B1', 'nutri_unit': 'mg'},
    {'nutri_amount': 29.96, 'nutri_name': 'Net Carbohydrates', 'nutri_unit': 'g'},
    {'nutri_amount': 889.84, 'nutri_name': 'Vitamin A', 'nutri_unit': 'IU'},
    {'nutri_amount': 11.62, 'nutri_name': 'Protein', 'nutri_unit': 'g'},
    {'nutri_amount': 108.96, 'nutri_name': 'Magnesium', 'nutri_unit': 'mg'},
    {'nutri_amount': 0.15,
    'nutri_name': 'Poly Unsaturated Fat',
    'nutri_unit': 'g'},
    {'nutri_amount': 0.91, 'nutri_name': 'Fat', 'nutri_unit': 'g'},
    {'nutri_amount': 0.0, 'nutri_name': 'Vitamin B12', 'nutri_unit': '�g'},
    {'nutri_amount': 332.33, 'nutri_name': 'Vitamin C', 'nutri_unit': 'mg'},
    {'nutri_amount': 97.16, 'nutri_name': 'Choline', 'nutri_unit': 'mg'},
    {'nutri_amount': 1543.6, 'nutri_name': 'Potassium', 'nutri_unit': 'mg'},
    {'nutri_amount': 390.44, 'nutri_name': 'Folate', 'nutri_unit': '�g'},
    {'nutri_amount': 1.45, 'nutri_name': 'Manganese', 'nutri_unit': 'mg'},
    {'nutri_amount': 2.12, 'nutri_name': 'Vitamin B3', 'nutri_unit': 'mg'},
    {'nutri_amount': 690.08, 'nutri_name': 'Vitamin K', 'nutri_unit': '�g'},
    {'nutri_amount': 0.0, 'nutri_name': 'Vitamin D', 'nutri_unit': '�g'},
    {'nutri_amount': 1.13, 'nutri_name': 'Vitamin B6', 'nutri_unit': 'mg'},
    {'nutri_amount': 0.0, 'nutri_name': 'Caffeine', 'nutri_unit': 'mg'},
    {'nutri_amount': 0.0, 'nutri_name': 'Alcohol', 'nutri_unit': 'g'},
    {'nutri_amount': 163.44, 'nutri_name': 'Sodium', 'nutri_unit': 'mg'},
    {'nutri_amount': 363.2, 'nutri_name': 'Calcium', 'nutri_unit': 'mg'},
    {'nutri_amount': 0.15,
    'nutri_name': 'Mono Unsaturated Fat',
    'nutri_unit': 'g'},
    {'nutri_amount': 22.7, 'nutri_name': 'Fiber', 'nutri_unit': 'g'},
    {'nutri_amount': 0.17, 'nutri_name': 'Copper', 'nutri_unit': 'mg'},
    {'nutri_amount': 1.92, 'nutri_name': 'Vitamin B5', 'nutri_unit': 'mg'},
    {'nutri_amount': 0.0, 'nutri_name': 'Folic Acid', 'nutri_unit': '�g'},
    {'nutri_amount': 227.0, 'nutri_name': 'Calories', 'nutri_unit': 'kcal'},
    {'nutri_amount': 0.36, 'nutri_name': 'Vitamin B2', 'nutri_unit': 'mg'},
    {'nutri_amount': 0.0, 'nutri_name': 'Cholesterol', 'nutri_unit': 'mg'},
    {'nutri_amount': 0.31, 'nutri_name': 'Saturated Fat', 'nutri_unit': 'g'},
    {'nutri_amount': 1.63, 'nutri_name': 'Zinc', 'nutri_unit': 'mg'},
    {'nutri_amount': 2.72, 'nutri_name': 'Selenium', 'nutri_unit': '�g'},
    {'nutri_amount': 1.36, 'nutri_name': 'Vitamin E', 'nutri_unit': 'mg'},
    {'nutri_amount': 236.08, 'nutri_name': 'Phosphorus', 'nutri_unit': 'mg'},
    {'nutri_amount': 9.08, 'nutri_name': 'Fluoride', 'nutri_unit': 'mg'},
    {'nutri_amount': 4.27, 'nutri_name': 'Iron', 'nutri_unit': 'mg'},
    {'nutri_amount': 29.06, 'nutri_name': 'Sugar', 'nutri_unit': 'g'}
]


for element in range(len(list)):
    if list[element]["nutri_name"] == "Calories":
        del list[element]
        break
"""



"""
url = f"https://api.spoonacular.com/food/ingredients/{9037}/information"
endpoint = f"{url}?apiKey={api_key}"
response = requests.get(endpoint, params={
    "amount": 1,
    "unit": "piece",
})

data = response.json()

main_nutrients = []

for main_nutri in data["nutrition"]["nutrients"]:
    if main_nutri["name"] == "Calories":
        calories_name = main_nutri["name"]
        calories_amount = main_nutri["amount"]
        calories_unit = main_nutri["unit"]

        main_nutrients.append(
            {
            "calories_name": calories_name,
            "calories_amount": calories_amount,
            "calories_unit": calories_unit,
            }
        )

    if main_nutri["name"] == "Carbohydrates":
        carbs_name = main_nutri["name"]
        carbs_amount = main_nutri["amount"]
        carbs_unit = main_nutri["unit"]

        main_nutrients.append(
            {
            "carbs_name": carbs_name,
            "carbs_amount": carbs_amount,
            "carbs_unit": carbs_unit,
            }
        )

pprint.pprint(main_nutrients)
"""