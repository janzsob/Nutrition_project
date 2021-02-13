from django.shortcuts import render, redirect
from .api_call import ingredient_info
from django.contrib import messages
from .forms import ProductSearchForm
from .models import TopIngredients, Units

"""
def get_product_id(request):
    if request.method == "POST":
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            request.session["product_id"] = form.cleaned_data.get("product_id") # using session to get and store product id
            #request.session["product_unit"] = form.cleaned_data.get("product_unit")
            #request.session["product_amount"] = form.cleaned_data.get("product_amount")
            return redirect("ingredient_app:search_results")

    else:
        form = ProductSearchForm()
    
    context = {"form": form}
    return render(request, "ingredient_app/search_page.html", context)


def search_results_view(request):
    product_id = request.session.get("product_id") # get product id from session
    #product_unit = request.session.get("product_unit")
    #product_amount = request.session.get("product_amount")
    api_request = ingredient_info(product_id)
    
    if api_request == "402 error": # in case of 402 error
        messages.add_message(request, messages.ERROR, "The app has reached the max daily request limit.")
        return redirect("ingredient_app:search_page")   
    elif api_request == "unit error":
        messages.add_message(request, messages.ERROR, "Invalid unit. Please choose another one.")
        return redirect("ingredient_app:search_page")   
    else:
        if api_request == KeyError: # in case of KeyError
            messages.add_message(request, messages.ERROR, "The given product doesn't exists in the database.")
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
"""

def get_product(request):
    product_name_input = request.GET.get("product_name_input")
    product_unit_input = request.GET.get("product_unit_input")
    product_amount = request.GET.get("product_amount_input")
    
    if product_name_input == "" or product_name_input is None:
        unit_list = Units.objects.all()
        """
        unit_list = []
        for unit in Units.objects.all().values("name"):
            unit_list.append(unit["name"])
        """
        
        context = {"unit_list": unit_list} # fors select options in form             
        return render(request, "ingredient_app/search_page.html", context)
    
    else:
        product_queryset = TopIngredients.objects.all()
        unit_queryset = Units.objects.all()

        product_id = product_queryset.filter(product_name__iexact=product_name_input).values("product_id")[0]["product_id"]
        product_unit = unit_queryset.filter(name__iexact=product_unit_input).values("name")[0]["name"]

        api_request = ingredient_info(product_id, product_amount, product_unit)

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