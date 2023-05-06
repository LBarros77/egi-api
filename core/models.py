from django.conf import settings
from django.db import models
import uuid
from datetime import datetime


class Addrees(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=4)
    postal_code = models.CharField(max_length=8)
    country = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'Addrees'

    def __str__(self):
        return f'{self.city}-{self.state}'


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to='images/categories')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# class User(models.Model):
#     name = models.CharField(max_length=120)
#     cpf = models.CharField(max_length=11)
#     email = models.EmailField(max_length=160)
#     password = modles.CharField(max_length=16)
#     image = models.ImageField(null=True, blank=True, upload_to='images/users')
#     skills = models.CharField(null=True, blank=True)
#     star = models.IntegerField(max_length=5)
#     created = models.DateTimeField(auto_now_add)


# class Manager(User):
#     cnpj = models.CharField(maxLength=14)
    
#     def __init__(self, *keys, **args):
#         self.


class Event(models.Model):
    addrees = models.ForeignKey(Addrees, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')
    manager = models.ManyToOneField('auth.User', on_delete=models.PROTECT, related_name='events')
    colaborator = models.ForeignKey(User[], on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    ticket = models.UUIDField(default=uuid.uuid4, editable=False)
    price = models.FloatField(default=0.00, null=True, blank=True)
    star = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/events')
    video_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

    def __str__(self):
        return self.name


# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()

# comment = Comment(email='leila@example.com', content='foo bar')