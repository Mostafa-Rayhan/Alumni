from django.db import models

# Create your models here.

class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # varsityEmail = models.EmailField(max_length=50, null=True, blank=True)
    # varsityId = models.CharField(max_length=25, null=True, blank=True)
    # linkedIn = models.CharField(max_length=500, null=True, blank=True)
    # password1 = models.CharField(max_length=20, null=True)
    # password2 = models.CharField(max_length=20, null=True)

    # check = models.BooleanField('Is check', default=False)

    username = None

    USERNAME_FIELD = 'varsityEmail'
    REQUIRED_FIELDS = ['varsityId', 'linkedIn', 'password1', 'password2']
    #
    # def __str__(self):
    #     return self.varsityEmail

class AlumniSheet(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.name
