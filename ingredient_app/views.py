from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request, "ingredient_app/home.html", context)