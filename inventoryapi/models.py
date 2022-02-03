from django.db import models
from django.utils.timezone import now


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    sku = models.CharField(max_length=40, default='')

    # created_date = models.DateTimeField(auto_now_add=True, default=now)

    def __str__(self):
        return self.sku

    class Meta:
        ordering = ('name',)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    note = models.CharField(max_length=40, default='')
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)


    product = models.OneToOneField(
        Product,
        default=1,
        on_delete=models.CASCADE
    )

    supplier = models.ForeignKey(Supplier, related_name='supplier_id',
                                 blank=False,
                                 null=True, default=1,
                                 on_delete=models.SET_NULL)

    # created_date = models.DateTimeField(auto_now_add=True, default=now)

    class Meta:
        ordering = ('stock',)


    def __str__(self):
        return self.name
