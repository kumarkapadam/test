from django.db import models

# Create your models here.
class Stundent_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25,blank=False,null=False)
    email =  models.EmailField()
    age = models.IntegerField()
    gender=models.CharField(max_length=50)

    def __str__(self):
        return self.name