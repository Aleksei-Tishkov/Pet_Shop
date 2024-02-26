from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(request_finished)
def post_save_product(sender, **kwargs):
    return
