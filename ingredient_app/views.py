from django.shortcuts import render, redirect
from .api_call import ingredient_info
from django.contrib import messages
from .models import TopIngredients, Units
from django.http import JsonResponse


def get_product(request):
    product_name_input = request.GET.get("product_name_input")
    product_unit_input = request.GET.get("product_unit_input")
    product_amount = request.GET.get("product_amount_input") # required param for api call

    unit_list = Units.objects.all() 

    if product_name_input == "" or product_name_input is None: # render the search page
        # to autocomplete the product name during typing
        if "term" in request.GET:
            qs = TopIngredients.objects.filter(product_name__istartswith=request.GET.get("term"))
            names = list()
            for item in qs:
                names.append(item.product_name)
            return JsonResponse(names, safe=False)
                
        context = {
            "unit_list": unit_list, # for select options in form
            }              
        return render(request, "ingredient_app/search_page.html", context)
    
    else:
        product_queryset = TopIngredients.objects.all()

        # Check wether the given product exists
        try:
            product_id = product_queryset.filter(product_name__iexact=product_name_input).values("product_id")[0]["product_id"] # required param for api call
        except(IndexError):
            messages.add_message(request, messages.ERROR, "The given product doesn't exists in the database.")
            return redirect("ingredient_app:search_page")
        
        product_unit = unit_list.filter(name__iexact=product_unit_input).values("name")[0]["name"] # required param for api call

        api_request = ingredient_info(product_id, product_amount, product_unit)

        """ Errors """
        if api_request == "402 error": # in case of 402 error
            messages.add_message(request, messages.ERROR, "The app has reached the max daily request limit.")
            return redirect("ingredient_app:search_page")
        elif api_request == "unit error":
            messages.add_message(request, messages.ERROR, "Invalid unit in case of this product. Please choose another one.")
            return redirect("ingredient_app:search_page")  
    
        
        for item in api_request:
            main_info = item["main_info"]
            nutrients_list = item["nutrients_list"]
            glycemic_list = item["glycemic_list"]
            calories_data = item["calories_data"][0]
            carbs_data = item["carbs_data"][0]
            protein_data = item["protein_data"][0]
            fat_data = item["fat_data"][0]

        # check whether the unit will be displayed in plural or not
        if int(product_amount) > 1:
            # plural name
            product_unit_display = unit_list.filter(name__iexact=product_unit_input).values("plural_name")[0]["plural_name"]
        else:
            product_unit_display = unit_list.filter(name__iexact=product_unit_input).values("name")[0]["name"]


        context = {
            "main_info": main_info,
            "nutrients_list": nutrients_list,
            "glycemic_list": glycemic_list,
            "calories_data": calories_data,
            "carbs_data": carbs_data,
            "protein_data": protein_data,
            "fat_data": fat_data,
            "product_unit_display": product_unit_display,
        }

        return render(request, "ingredient_app/search_results.html", context)