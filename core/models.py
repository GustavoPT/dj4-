from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User as DjangoUser

class Product(models.Model):
    image_path = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    price = models.FloatField()
    author_name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=128)
    genre = models.CharField(max_length=32)
    product_type = models.CharField(max_length=32)  # New field to indicate product type

    def get_all_products():
        return Product.objects.all()

    def get_product(product_id):
        return Product.objects.filter(id=product_id).first()

    def delete_product(product_id):
        return Product.objects.filter(id=product_id).delete()

    def update_product_price(product_id, price):
        product_to_update = Product.objects.filter(id=product_id).first()
        if product_to_update:
            product_to_update.price = price
            product_to_update.save()

    def update_product_title(product_id, title):
        product_to_update = Product.objects.filter(id=product_id).first()
        if product_to_update:
            product_to_update.title = title
            product_to_update.save()

    def __str__(self):
        return self.title


class User(DjangoUser):  # Extending Django's built-in user model
    shipping_address = models.CharField(max_length=128)
    credit_card_num = models.CharField(max_length=128)
    exp_date = models.CharField(max_length=128)
    cvs = models.IntegerField()
    name_on_card = models.CharField(max_length=128)
    products = models.ManyToManyField(Product, through='ProductCopy')

    def __str__(self):
        return self.username

 
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title}"


class ProductCopy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title}"

