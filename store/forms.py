from django.forms import ChoiceField, Textarea, ModelForm, ModelChoiceField

from store.models import Order, Product, Distributor


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('slug', 'name', 'category', 'price', 'description',)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = Textarea({'rows': 3})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

        # Make `slug` attribute uneditable
        if self.instance.slug != '':
            del self.fields['slug']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'distributor', 'paid', 'fee', 'deadline', 'note',)

    def __init__(self, product=None, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        if product is not None:
            self.fields['product'].initial=product
            self.fields['distributor'] = ModelChoiceField(
                queryset=Distributor.objects.filter(product=product),
            )
        self.fields['note'].widget = Textarea({'rows': 3})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
