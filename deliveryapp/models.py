from django.db import models

# Create your models here.
class restaurant_register(models.Model):
    restaurant_name = models.CharField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.restaurant_name

class food_details(models.Model):
    restaurant = models.ForeignKey(restaurant_register,on_delete=models.CASCADE)
    foodname = models.CharField(max_length=50,null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.name
