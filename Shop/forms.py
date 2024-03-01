from django import forms
from django.forms import formset_factory

from Shop.models import Product, ProductPhoto, Cart
from bootstrap_modal_forms.forms import BSModalModelForm

from Shop.services import get_product_by_slug, get_available_products, get_cart_entry_by_pk


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
        fields = ('product_name', 'product_main_photo', 'slug', 'product_short_description', 'product_description',
                  'product_price', 'product_quantity', 'product_is_published')
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control back-drop'}),
            'product_main_photo': forms.FileInput(attrs={'class': 'upload__file'}),
            'slug': forms.TextInput(attrs={'class': 'form-control back-drop'}),
            'product_short_description': forms.Textarea(attrs={'class': 'form-control back-drop', 'rows': 2}),
            'product_description': forms.Textarea(attrs={'class': 'form-control back-drop', 'rows': 5}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control back-drop'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'form-control back-drop'}),
            'product_is_published': forms.CheckboxInput(attrs={'class': "form-check-input",
                                                               'type': "checkbox",
                                                               'role': "switch"}
                                                        )

        }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={'class': 'upload__file'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ProductImagesForm(forms.Form):
    product_photo = MultipleFileField(required=False)
    use_required_attribute = False


class CartAdditionForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        _obj = get_product_by_slug(get_available_products(), str(kwargs['request']).split('/')[-2])
        super().__init__(*args, **kwargs)
        self.fields['quantity'] = forms.IntegerField(max_value=_obj.last().product_quantity,
                                                     min_value=1,
                                                     widget=forms.NumberInput(attrs={
                                                         'style': 'width: 30%',
                                                         'class': 'ps-2',
                                                         'value': 1}))

    class Meta:
        model = Cart
        fields = ('quantity',)


class CartEntryChange(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        _instance = kwargs['instance']
        _obj = _instance.product
        super().__init__(*args, **kwargs)
        self.fields['quantity'] = forms.IntegerField(max_value=_obj.product_quantity,
                                                     min_value=1,
                                                     widget=forms.NumberInput(attrs={
                                                         'style': 'width: 30%',
                                                         'class': 'ps-2',
                                                         'value': _instance.quantity}))
        self.name = _obj

    class Meta:
        model = Cart
        fields = ('quantity',)


class CartDeleteForm(BSModalModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['customer_postalcode'].required = True
        self.fields['customer_address'].required = True
        self.fields['customer_postalcode'] = forms.IntegerField(max_value=999999,
                                                                min_value=1,
                                                                widget=forms.NumberInput(attrs={
                                                                    'class': 'form-control col-3 back-drop'
                                                                }))

    class Meta:
        model = Cart
        fields = ('customer_postalcode', 'customer_address',)
        widgets = {'customer_address': forms.TextInput(attrs={'class': 'form-control col-7 back-drop'})}
