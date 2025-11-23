from django.db import models
class useddata(models.Model):
   username=models.CharField(max_length=100)
   Email=models.EmailField()
   password=models.CharField(max_length=100)
   ConfirmPassword=models.CharField(max_length=100)
   class Meta:
    db_table="useddata"
# models.py
from django.db import models
#from django.utils import timezone

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Fashion', 'Fashion'),
        ('Electronics', 'Electronics'),
        ('Jewellery', 'Jewellery'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    
    
    def _str_(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=40, blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity

    


