from django.db import models

# Create your models here.

class Storage(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to = 'photos/%y/%m/%d', default='default_image.jpg')
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name

