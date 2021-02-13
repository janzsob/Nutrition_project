from django.urls import path
from . import views

app_name = "ingredient_app"
urlpatterns = [
    path("", views.get_product, name="search_page"),
    path("results/", views.get_product, name="search_results")
]
