from django.test import TestCase
from django.urls import reverse

from .models import Product


def create_product(slug, name, category, price, active=True):
    return Product.objects.create(
        slug=slug,
        name=name,
        category=category,
        price=price,
        active=active)


class ProductsListViewTests(TestCase):
    def test_no_products(self):
        response = self.client.get(reverse('store:list_products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '产品列表 (0)')
        self.assertQuerysetEqual(response.context['all_products'], [])


class ProductDetailViewTests(TestCase):
    def test_nonexist_product(self):
        response = self.client.get(reverse('store:view_product', args=('p1',)))
        self.assertEqual(response.status_code, 404)
