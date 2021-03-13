from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ReceiptLineItem


@receiver(post_save, sender=ReceiptLineItem)
def update_on_save(sender, instance, created, **kwargs):

    """ 
    Update total cost on lineitem updated or created
     """

    instance.receipt.update_total_cost()

@receiver(post_delete, sender=ReceiptLineItem)
def update_on_delete(sender, instance, **kwargs):

    """ 
    Update total cost on lineitem deleted
     """

    instance.receipt.update_total_cost()