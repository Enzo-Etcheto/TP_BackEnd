from django.db import models

# Create your models here.
class Autos(models.Model):
    marca=models.CharField(max_length=128)
    modelo=models.CharField(max_length=128)
    color=models.CharField(max_length=128)
    num_serie=models.IntegerField()

    def __str__(self):
        return f'{self.marca} - {self.modelo}- {self.color}- {self.num_serie}'

class User(models.Model):
    name=models.CharField(max_length=30)
    auto=models.ManyToManyField(Autos,blank=True)

    def __str__(self):
        return f'{self.name}-{self.auto}'