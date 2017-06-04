from django.db import models

# Create your models here.

ROLE_TYPE = (
		('AD', 'admin'),
		('RE', 'regular')
	)
class TeamMembers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=2, choices=ROLE_TYPE, default='RE')

		
class Test(models.Model):
	nzme = models.CharField(max_length = 10)