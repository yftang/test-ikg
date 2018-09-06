from django.forms import ChoiceField, Textarea, ModelForm, ModelChoiceField

from store.models import Order, Product, Distributor


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
        if len(args) > 0 and 'product' in args[0]:
            product = args[0]['product']
            print('Product: %s' % product)
            self.fields['product'] = ModelChoiceField(
                queryset=Product.objects.all(),
                initial=product,
            )
            self.fields['distributor'] = ModelChoiceField(
                queryset=Distributor.objects.filter(product=product),
            )
        self.fields['note'].widget = Textarea({'rows': 3})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
