from django import forms
from.models import Items1
class ItemForm(forms.ModelForm):
    class Meta:
        model=Items1
        fields=['item_name1','item_desc1','item_price1','item_image']
