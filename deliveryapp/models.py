from django.db import models

# Create your models here.
class food_details(models.Model):
    foodname = models.CharField(max_length=50,null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.name

class register_models(models.Model):
    restaurant_name = models.CharField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title