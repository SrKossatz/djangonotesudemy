from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta: #django model meta options
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null = True, blank = True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='picture/%Y/%m/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
