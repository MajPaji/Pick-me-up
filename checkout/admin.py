from django.contrib import admin
from .models import Receipt, ReceiptLineItem


class ReceiptLineItemAdminInline(admin.TabularInline):
    model = ReceiptLineItem
    readonly_fields = ('lineitem_total',)


class ReceiptAdmin(admin.ModelAdmin):
    inlines = (ReceiptLineItemAdminInline,)

    readonly_fields = ('receipt_number', 'date',
                       'total_cost', 'total_plus_tax')

    fields = ('receipt_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address',
              'total_cost', 'total_plus_tax')

    list_display = ('receipt_number', 'date', 'full_name',
                    'total_cost', 'total_plus_tax')

    ordering = ('-date',)


admin.site.register(Receipt, ReceiptAdmin)
