from django.db.models import QuerySet
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver
from Pet_Shop.settings import PAYPAL_BUSINESS_EMAIL
from Shop.services import get_cart_entry_by_pk, get_cart_sum, process_cart


@receiver(valid_ipn_received)
def paypal_checker_success(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == 'Completed':
        if ipn_obj.receiver_email != PAYPAL_BUSINESS_EMAIL:
            # Not a valid payment
            return
        #if float(ipn_obj.mc_gross) != cart_sum or ipn_obj.mc_currency != 'USD':
            #print(float(ipn_obj.mc_gross), cart_sum)
            # Not a valid payment sum or currency
            return
        process_cart(ipn_obj.item_name)

        print('payment successful')



@receiver(invalid_ipn_received)
def paypal_checker_success(sender, **kwargs):
    print('Payment unsuccessful')
