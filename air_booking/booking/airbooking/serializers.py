from rest_framework import serializers
from .models import Passenger


class Passengers_api(serializers.Serializer):
	name = serializers.CharField(max_length=100)
	age =  serializers.IntegerField()
	sex =  serializers.CharField(max_length=15)
	number =  serializers.CharField(max_length=15)
	boarding =  serializers.CharField(max_length=20)
	depature =  serializers.CharField(max_length=20)
	seat_no = serializers.CharField(max_length=20)
	adaar =  serializers.IntegerField()
		
	def create(self,validate_data):
		return Passenger.objects.create(**validate_data)
