from django.db import models
from django.utils import timezone

class Cateory(models.Model):
    name = models.CharField(max_length=100)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null = True, blank = True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='picture/%Y/%m/', blank=True)
    category = models.ForeignKey(Cateory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
