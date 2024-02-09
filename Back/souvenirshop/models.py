
from django.db import models

class Souvenir(models.Model):
    souvenir_code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='products_photo/', null=True, blank=True)

    def __str__(self):
        return self.name
