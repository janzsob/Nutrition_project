import csv
from ingredient_app.models import TopIngredients

csv_path = "C:/Users/bence/Python/APIs/Spoonacular_API/spoon_env/nutrition_project/ingredient_app/static/ingredient_app/top-1k-ingredients.csv"

def run(): # the function must be called run.
    TopIngredients.objects.all().delete()

    with open(csv_path, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            TopIngredients.objects.create(product_name=row[0], product_id=row[1])


# run it in terminal: python manage.py runscript loading_csv

