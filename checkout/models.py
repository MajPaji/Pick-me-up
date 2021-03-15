from django.db import models
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from django_countries.fields import CountryField


class Receipt(models.Model):
    receipt_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=55, null=False, blank=False)
    email = models.EmailField(max_length=275, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=25, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_plus_tax = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_receipt_id(self):
            """
            Generate a random, unique receipt number using UUID
            """
            return uuid.uuid4().hex.upper()

    def update_total_cost(self):
        """
        Update total cost and total cost plus tax,
        everytime a new item added to the receipt.
        """
        self.total_cost = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.total_plus_tax = self.total_cost + self.total_cost * settings.TAX_PERCENTAGE / 100
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the receipt number
        if it hasn't been set already.
        """
        if not self.receipt_number:
            self.receipt_number = self._generate_receipt_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.receipt_number


class ReceiptLineItem(models.Model):
    receipt = models.ForeignKey(Receipt, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the total cost.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Receipt number: {self.receipt.receipt_number}, product name : {self.product.name} '


