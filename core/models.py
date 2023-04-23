from django.conf import settings
from django.db import models
from datetime import datetime


# User = settings.AUTH_USER_MODEL

class Addrees(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=4)
    postal_code = models.CharField(max_length=8)
    country = models.CharField(max_length=120)


# class User(models.Model):
#     name = models.CharField(maxLength=120)
#     cpf = models.CharField(maxLength=11)
#     email = models.CharField(maxLength=160)
#     password = modles.CharField(maxLength=16)
#     star = models.IntegerField(size=5)


# class Manager(User):
#     cnpj = models.CharField(maxLength=14)
    
#     def __init__(self, *keys, **args):
#         self.


class Event(models.Model):
    CATEGORIES = (
        ('00', 'Geral'),
        ('01', 'Esportes'),
        ('02', 'Cultura'),
    )
    # colaborator = models.ForeignKey(User[])
    addrees = models.ForeignKey(Addrees, blank=True, null=True, on_delete=models.SET_NULL)
    # manager = models.ManyToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    category = models.CharField(choices=CATEGORIES, default='Geral', max_length=100)
    description = models.TextField(null=True, blank=True)
    ticket = models.CharField(max_length=8, null=True, blank=True)
    price = models.FloatField(default=0.00, null=True, blank=True)
    star = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    photo_url = models.CharField(max_length=40, null=True, blank=True)
    video_url = models.CharField(max_length=40, null=True, blank=True)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

# comment = Comment(email='leila@example.com', content='foo bar')