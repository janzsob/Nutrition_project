from django.urls import path
from . import views

app_name = "ingredient_app"
urlpatterns = [
    path("", views.search_page_view, name="search_page"),
    path("results/", views.search_results_view, name="search_results")
]
