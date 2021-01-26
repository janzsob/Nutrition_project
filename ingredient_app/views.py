from django.shortcuts import render, redirect
from .api_call import ingredient_info
from django.contrib import messages


def search_page_view(request):
    if request.method == "POST":
        request.session["product_id"] = request.POST.get("product_id") # using session to get and store product id
        return redirect("ingredient_app:search_results")
    else:    
        context = {}
        return render(request, "ingredient_app/search_page.html", context)

def search_results_view(request):
    product_id = request.session.get("product_id") # get product id from session
    api_request = ingredient_info(product_id)
    
    if api_request == "402 error": # in case of 402 error
        messages.add_message(request, messages.ERROR, "The app has reached the max daily request limit.")
        return redirect("ingredient_app:search_page")   
    else:
        if api_request == KeyError: # in case of KeyError
            messages.add_message(request, messages.ERROR, "The given Id doesn't exists.")
            return redirect("ingredient_app:search_page")
        else: # The ideal way
            for item in api_request:
                main_info = item["main_info"]
                nutrients_list = item["nutrients_list"]
                glycemic_list = item["glycemic_list"]
                calories_data = item["calories_data"][0]
                carbs_data = item["carbs_data"][0]
                protein_data = item["protein_data"][0]
                fat_data = item["fat_data"][0]


            context = {
                "main_info": main_info,
                "nutrients_list": nutrients_list,
                "glycemic_list": glycemic_list,
                "calories_data": calories_data,
                "carbs_data": carbs_data,
                "protein_data": protein_data,
                "fat_data": fat_data,
            }

    return render(request, "ingredient_app/search_results.html", context)