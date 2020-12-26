from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime
from django.contrib.postgres.fields import ArrayField


class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    authors = models.ManyToManyField(Author,related_name="authors")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    desc = models.TextField()
    image = models.ImageField(upload_to='product_images', db_column='Image', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book,related_name="books",through="Count",null=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}'s Cart".format(self.user)


class Entry(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.book.name)

class Count(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} number of {} book available in cart {}".format(self.count,self.book,self.cart)

@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.book.price
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = datetime.now()