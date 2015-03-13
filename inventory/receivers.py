from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import CSV
from integration.tasks import csv_insert

@receiver(post_save, sender=CSV)
def my_handler(sender, instance, **kwargs):
    csv_insert.delay(instance)
