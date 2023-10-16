from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    sumary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=True) #null=True or default=True (por se bool) para preenchar os antigos já adicionados