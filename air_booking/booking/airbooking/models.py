from django.db import models

class Passenger(models.Model):
	date = models.DateField(auto_now=True)
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	sex = models.CharField(max_length=15,default='male',blank=True)
	number = models.CharField(max_length=15)
	boarding = models.CharField(max_length=20)
	depature = models.CharField(max_length=20)
	seat_no =models.CharField(max_length=20,default='null')
	adaar = models.IntegerField()

	def __str__(self):
		if self.name == None:
			return 'Error'
		return self.name

	
