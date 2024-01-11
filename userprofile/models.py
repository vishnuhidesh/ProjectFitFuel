from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    abdomen = models.FloatField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    diabetic = models.CharField(max_length=20, choices=[
        ('diabetic', 'Diabetic'),
        ('not_diabetic', 'Not Diabetic'),
        ('not_sure', 'Not Sure'),
    ], default='not_sure')

    def __str__(self):
        return self.user.username