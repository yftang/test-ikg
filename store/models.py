from django.db import models


class Distributor(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, primary_key=True)

    class Meta:
        ordering = ('slug',)

    def __repr__(self):
        return '<Distributor {0}: {1}>'.format(self.slug, self.name)


class Product(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, primary_key=True)
    category = models.CharField(max_length=32)
    price = models.IntegerField()
    description = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    distributors = models.ManyToManyField(Distributor)

    class Meta:
        indexes = [
            models.Index(fields=['category'], name='category_idx'),
        ]
        ordering = ('category', 'slug',)

    def __repr__(self):
        return '<Product {0}: {1}>'.format(self.slug, self.name)


class Order(models.Model):
    deadline = models.DateTimeField(blank=True)
    note = models.CharField(max_length=200, blank=True)
    fee = models.IntegerField(blank=True)
    paid = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    distributor = models.ForeignKey('Distributor', on_delete=models.SET_NULL, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['deadline'], name='deadline_idx'),
            models.Index(fields=['paid'], name='paid_idx'),
        ]
        ordering = ('deadline',)

    def __repr__(self):
        return '<Order #{0}: {1}>'.format(self.id, self.product.name)
