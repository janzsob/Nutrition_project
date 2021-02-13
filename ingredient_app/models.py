from django.db import models

class TopIngredients(models.Model):
    product_name = models.CharField("Product Name", max_length=50)
    product_id = models.IntegerField("Product ID")
    
    

    class Meta:
        verbose_name = "TopIngredient"
        verbose_name_plural = "TopIngredients"
        ordering = ["product_name"]

    def __str__(self):
        return self.product_name

class Units(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"

    def __str__(self):
        return self.name

