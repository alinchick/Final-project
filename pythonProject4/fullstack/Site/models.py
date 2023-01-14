from django.db import models


class Pic_Vos(models.Model):
    title = models.TextField()
    picture = models.ImageField(upload_to='vos/')

    def __str__(self):
        return self.title

class Pic_Geo(models.Model):
    tit = models.TextField()
    pic = models.ImageField(upload_to='geo/')

    def __str__(self):
        return self.tit
