from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.forms import ModelChoiceField

from .models import Distributor, Order, Product
from .forms import OrderForm, ProductForm


class ProductsList(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


class ProductsCreate(generic.CreateView):
    form_class = ProductForm
    success_url = reverse_lazy('store:list_products')
    template_name = 'products/create.html'


class ProductsDetail(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


class ProductsMgmtDistributions(generic.TemplateView):
    template_name = 'products/distribution_mgmt.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, slug=kwargs['slug'])
        related_distributors = product.distributors.all()
        unrelated_distributors = Distributor.objects.exclude(slug__in=related_distributors.values('slug')).all()
        context['product'] = product
        context['related_distributors'] = related_distributors
        context['unrelated_distributors'] = unrelated_distributors
        return context


class ProductsToggleDistributor(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('store:mgmt_product_distributions', args=(kwargs['pslug'],))

    def post(self, *args, **kwargs):
        pslug = kwargs['pslug']
        dslug = kwargs['dslug']
        p = get_object_or_404(Product, slug=pslug)
        d = get_object_or_404(Distributor, slug=dslug)

        if dslug in list(map(lambda d: d.slug, p.distributors.all())):
            p.distributors.remove(d)
        else:
            p.distributors.add(d)

        return super(ProductsToggleDistributorView, self).post(*args, **kwargs)


class ProductsUpdate(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('store:list_products')
    template_name = 'products/update.html'


class ProductsDelete(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('store:list_products')


class OrdersList(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        return Order.objects.all()


class OrdersCreate(generic.CreateView):
    form_class = OrderForm
    success_url = reverse_lazy('store:list_orders')
    template_name = 'orders/create.html'

    def get_form(self, *args, **kwargs):
        if 'product' in self.request.GET:
            product = self.request.GET['product']
            form = OrderForm({'product': product})
            return form
            # form.fields['product'] = ModelChoiceField(queryset=Product.objects.all(), initial=product)
            # form.fields['distributor'] = ModelChoiceField(queryset=Distributor.objects.filter(product=Product))

        return OrderForm()


class OrdersDetail(generic.DetailView):
    model = Order
    template_name = 'orders/detail.html'
    context_object_name = 'order'


class OrdersUpdate(generic.UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('store:list_orders')
    template_name = 'orders/update.html'


class OrdersDelete(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('store:list_orders')
