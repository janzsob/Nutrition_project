from django import forms
from .pd import choices_list # exported data from CSV file

unit_choices = [
    ("piece", "piece"),
    ("fruit", "fruit"),
    ("g", "g"),
    ("cup", "cup"),
    ("teaspoon", "teaspoon"),
    ("tablespoon", "tablespoon"),
    ("drink box", "drink box"),
]

class ProductSearchForm(forms.Form):
    product_id = forms.ChoiceField(choices=choices_list)
    """
    product_unit = forms.ChoiceField(choices=unit_choices, required= True)
    product_amount = forms.IntegerField(min_value=1, error_messages= {
        "min_value": "This value cannot be lower than 1.",
    })
    """
