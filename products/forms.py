from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(required=False ,label='', widget=forms.TextInput(
        attrs={
            "placeholder": "Wirite a title",    
        }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name",
        "id": "my-id-for-textarea",
        "rows": 20,
        "cols": 120,
    }))
    price = forms.DecimalField(required=False ,initial=200)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ] 

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if not "kelvin" in title:
            raise forms.ValidationError("O titulo precisa ter a palavra: kelvin")

        return title

class RawProdoctForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            "placeholder": "Wirite a title",    
        }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name",
        "id": "my-id-for-textarea",
        "rows": 20,
        "cols": 120,
    }))
    price = forms.DecimalField(initial=200)


    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if not "kelvin" in title:
            raise forms.ValidationError("O titulo precisa ter a palavra: kelvin")

        return title

class UpdateProdoctForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ] 


    # def clean_product_id(self, *args, **kwargs):
    #     product_id = self.cleaned_data.get('product_id')
    #     queryset = Product.objects.all()
        
    #     available_ids = map(self.take_id, queryset)

    #     print(available_ids)

    #     if not "kelvin" in title:
    #         raise forms.ValidationError("O titulo precisa ter a palavra: kelvin")

    #     return title
    
    # def take_id(self, instance):
    #     return instance.id