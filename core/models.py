from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


