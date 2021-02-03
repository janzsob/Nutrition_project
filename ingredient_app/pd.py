import pandas as pd 
import pprint

df = pd.read_csv(r"C:\Users\bence\Python\APIs\Spoonacular_API\spoon_env\nutrition_project\ingredient_app\static\ingredient_app\top-1k-ingredients.csv", delimiter=';', header=None)
df.columns = ["product_name", "product_id"]

#vas = df[df.product_id == 9070]
#print(type(vas.iloc[0, 0]))

""" Export data from CSV file"""

name = df.loc[:,"product_name"]
id = df.loc[:,"product_id"]

choices_list = []
for n in range(len(name)):
    #print(f"{name[n]} - {id[n]}")
    sub_list = []
    sub_list.append(id[n])
    sub_list.append(name[n])
    
    choices_list.append(sub_list)

#pprint.pprint(choices_list)

