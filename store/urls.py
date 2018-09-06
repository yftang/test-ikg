from django.urls import path

from . import views


app_name = 'store'
urlpatterns = [
    path('', views.ProductsList.as_view(), name='list_products'),
    path('products/create', views.ProductsCreate.as_view(), name='create_product'),
    path('product/<slug:slug>', views.ProductsDetail.as_view(), name='view_product'),
    path('product/<slug:slug>/update', views.ProductsUpdate.as_view(), name='update_product'),
    path('product/<slug:slug>/delete', views.ProductsDelete.as_view(), name='delete_product'),
    path('product/<slug:slug>/mgmt_distributions', views.ProductsMgmtDistributions.as_view(), name='mgmt_product_distributions'),
    path('product/<slug:pslug>/toggle_distributor/<slug:dslug>', views.ProductsToggleDistributor.as_view(), name='toggle_product_distributor'),

    path('orders', views.OrdersList.as_view(), name='list_orders'),
    path('orders/create', views.OrdersCreate.as_view(), name='create_order'),
    path('order/<int:id>', views.OrdersDetail.as_view(), name='view_order'),
]
