from django.db import models


class Addrees(models.Model):
    street = models.CharField(maxLength=150)
    city = models.CharField(maxLength=150)
    state = models.CharField(maxLength=4)
    postal_code = models.CharField(maxLength=8)
    country = models.CharField(maxLength=120)


class User(models.Model):
    name = models.CharField(maxLength=120)
    cpf = models.CharField(maxLength=11)
    email = models.CharField(maxLength=160)
    password = modles.CharField(maxLength=16)
    star = models.IntegerField(size=5)


class Manager(User):
    cnpj = models.CharField(maxLength=14)
    def __init__(self, *keys, **args):
        self.


class Event(models.Model):
    CATEGORIES = (
        ('01', 'Esportes'),
        ('02', 'Cultura'),
        ('03', '')
    )
    colaborator = models.ForeignKey(User[])
    addrees = models.ForeignKey(Addrees, on_delete=models.CASCADE)
    manager = models.ManyToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(maxLength=120)
    date = models.DateField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    category = models.CharField(maxLength=100, choices=CATEGORIES)
    details = models.TextField()
    ticket = models.CharField(maxLength=8)
    price = models.FloatField()
    star = models.IntegerField(size=5)
    capacity = models.IntegerField(size=20000)
    photo_url = models.CharField(maxLength=40)
    video_url = models.CharField(maxLength=40)
