from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    data = models.DateTimeField(auto_now=True)
    price = models.CharField(max_length=50)
    is_exist = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    context = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
