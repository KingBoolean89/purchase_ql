from django.db import models


class ProductModel(models.Model):
    Segement = models.CharField(max_length=150)
    Country = models.CharField(max_length=150)
    Product = models.CharField(max_length=150)
    Units = models.IntegerField()
    Sales = models.IntegerField()
    Datesold = models.CharField(max_length=150)

    def __str__(self):
        return self.product
