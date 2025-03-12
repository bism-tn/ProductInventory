from django.db import models

class ProductModel(models.Model):

    name = models.CharField(max_length=50)

    category = models.CharField(max_length=50)

    price= models.DecimalField(decimal_places=2,max_digits=10)

    quantity = models.IntegerField()

    date_added =  models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name