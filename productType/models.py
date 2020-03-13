from django.db import models


# Create your models here.
class ProductType(models.Model):  # The Model is what will create the database for the product. 
    name = models.CharField(max_length=25, blank='')  # Empty default will not add a default product into the database.

    # description = models.TextField()  # A box into which you can type text about your product.
    # price = models.DecimalField(max_digits=6, decimal_places=2)  # To add a price which is no larger that 6 digits and has a decimal placing after 2 digits.
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name