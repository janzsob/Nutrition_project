from django.shortcuts import render, redirect
from .api_call import ingredient_info
from django.contrib import messages


def search_page_view(request):
    if request.method == "POST":
        request.session["product_id"] = request.POST.get("product_id")
        return redirect("ingredient_app:search_results")
    else:    
        context = {}
        return render(request, "ingredient_app/search_page.html", context)

def search_results_view(request):
    try:
        product_id = request.session.get("product_id")
        context = {"items": ingredient_info(product_id)}
    except(KeyError):
        messages.add_message(request, messages.ERROR, "The given Id doesn't exists.")
        return redirect("ingredient_app:search_page") # it needs to be added error message
    
    return render(request, "ingredient_app/search_results.html", context)