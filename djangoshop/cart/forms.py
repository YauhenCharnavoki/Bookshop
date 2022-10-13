from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    first_name = forms.CharField(label = "First name:", widget = forms.TextInput)
    last_name = forms.CharField(label = "Last name:", widget = forms.TextInput)
    phone_number = forms.CharField(label = "Phone number:", widget = forms.TextInput)
    email = forms.CharField(label = "Email:", widget = forms.TextInput)
    city = forms.CharField(label = "City:", widget = forms.TextInput)
    address = forms.CharField(label = "Address:", widget = forms.TextInput)
    card_number = forms.CharField(label = "Card_number:", widget = forms.TextInput)
    card_term= forms.CharField(label = "Card_term:", widget = forms.TextInput)
    cvv = forms.CharField(label = "CVV:", widget = forms.TextInput)
    
    class Meta:
        model = Purchase
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'city', 'address', 'card_number', 'card_term', 'cvv')

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class UpdateForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES, coerce = int)
    update = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)