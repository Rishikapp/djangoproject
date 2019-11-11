from django.db import models


class Abc(models.Model):
    Head = models.CharField(max_length=50)
    Descr = models.CharField(max_length=100)
    Date = models.DateField(auto_now_add=True, null=True, blank=True)
    Img = models.ImageField(upload_to='Qwerty')
