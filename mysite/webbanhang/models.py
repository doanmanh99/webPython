from django.contrib.auth.models import AbstractUser
from django.db import models



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# class CustomerUser(AbstractUser):
#     phone_number = models.CharField(default='', max_length=15)
#     address = models.CharField(default='', max_length=255)

class Category(models.Model):
    title = models.CharField(default='', max_length=100)
    # slug = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    product_img = models.CharField(max_length=255, default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    product_img = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    promo_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
#
# class Variation(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(default='', max_length=100)
#     price = models.IntegerField(default=0)
#     sale_price = models.IntegerField(default=0)
#     inventory = models.IntegerField(default=True)
#     active = models.BooleanField(default=True)
#
# class Cart(models.Model):
#     user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     item = models.ForeignKey(Variation, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)
#
# class Order(models.Model):
#     user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     shipping_address = models.CharField(max_length=255, default='')
#     order_description = models.TextField(default='')
#     is_complete = models.BooleanField(default=False)


