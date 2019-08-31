from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class PetModel(models.Model):
	owner=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	available=models.BooleanField(default=True)
	image=models.ImageField(null=True, blank=True)
	price=models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('pet-detail', kwargs={'pet_id':self.id})

