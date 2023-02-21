from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug']

    #     widgets = {
    #         'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
    #     }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['image'].widget.attrs.update({
    #         'placeholder': 'Upload Image',
    #         'aria-label': 'Upload Image'
    #     })