from django.db import models
from django.contrib.auth.models import User # type: ignore

# Create your models here.
CATEGORY = (
    ('Stationary', 'Papelería'),
    ('Electronics', 'Electrónica'),
    ('Food', 'Alimentos'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'{self.product}-{self.order_quantity} ordered by {self.staff.username}'
    
class PDF(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pdfs')
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)