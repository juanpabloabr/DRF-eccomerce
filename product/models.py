from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Supplier(models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(Base):
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier,related_name='Suppliers',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='Categories',on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    SKU = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        unique_together = ['SKU']

    def __str__(self):
        return self.name


class Review(Base):
    product = models.ForeignKey(Product,related_name='reviews',on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField(blank=True,default='')
    rating = models.DecimalField(max_digits=2,decimal_places=1)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        unique_together = ['email','product']

    def __str__(self):
        return f'{self.user_name} review the product {self.product} with rating {self.rating}'

    
