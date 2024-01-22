from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places = 2,max_digits = 10)
    
    @property
    def discount_price(self):
        return "%.2f" % ((float(self.price))- (float(self.price)*0.2))