from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class CustomerProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  dp = models.ImageField(upload_to="dp/", null=True)
  about = models.CharField(max_length=150, default="I am a customer", null=True)
  address = models.CharField(max_length=500, null=True)
  credit_rating = models.IntegerField(null=True, default="500")

  def __str__(self):
    return str(self.user)