from django import forms

from productapp.models import ProductModel

class AddproductForm(forms.ModelForm):

    class Meta:

        model = ProductModel

        fields = ["name","category","price","quantity"]

        widgets={
            'name' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the name"}),
            'category' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the Category"}),
            'price' : forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter the price"}),
            'quantity' : forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter the Quantity"}),
            
        }
