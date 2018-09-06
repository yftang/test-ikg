from django.forms import ChoiceField, Textarea, ModelForm

from .models import Order, Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('slug', 'name', 'category', 'price', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = Textarea({'rows': 3})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

        # Make `slug` attribute uneditable
        if self.instance.slug != None:
            del self.fields['slug']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'distributor', 'paid', 'fee', 'deadline', 'note',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'product' in kwargs:
            product = kwargs.pop('product')
            self.fields['distributor'] = ModelChoiceField(queryset=Distributor.objects.filter(product=product))
        self.fields['note'].widget = Textarea({'rows': 3})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
