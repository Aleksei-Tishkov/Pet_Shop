from django import forms

from Shop.models import Product, ProductPhoto


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_short_description', 'product_description',
                  'product_price', 'product_quantity')
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control back-drop'}),
            'product_short_description': forms.Textarea(attrs={'class': 'form-control back-drop', 'rows': 2}),
            'product_description': forms.Textarea(attrs={'class': 'form-control back-drop', 'rows': 5}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control back-drop'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'form-control back-drop'})
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {}


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductPhoto
        fields = ('product_photo',)

    product_photo = forms.ImageField(
        label='Product photos',
        widget=MultipleFileField()
    )


class ProductImagesForm(forms.Form):
    product_photo = MultipleFileField()