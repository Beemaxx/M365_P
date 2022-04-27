from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
License_type = (
    ('e-Licence', 'e-Licence'),
    ('Box', 'Box')
)
class Product(models.Model):
    
    product_name = models.CharField(max_length=200)
    vendor = models.ForeignKey( 
                                'Vendor',
                                on_delete=models.CASCADE,
                                null=False
    )
    
    price = models.DecimalField(max_digits= 10, decimal_places= 0)
    discount_voucher = models.DecimalField(max_digits= 3, decimal_places= 2, null = True, blank= True)
    # amount = models.IntegerField(default=1, 
    #                              validators= [
    #                                  MaxValueValidator(300),
    #                                  MinValueValidator(1)
    #                              ])
    license_type = models.CharField(max_length=200, choices = License_type,default='e-license')
    
    def __str__(self):
        return self.product_name
        
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs = {
            'id' : self.id
        })
        
    def get_remove_to_cart_url(self):
        return reverse("remove-to-cart", kwargs = {
            'id' : self.id
        })



class Vendor(models.Model):
    vendorname = models.CharField(max_length=200, blank=False)
    
    
    def __str__(self):
            return self.vendorname
        
    def get_absolute_url(self):
        return reverse("vendor-detail", kwargs={"pk": self.pk})
        
