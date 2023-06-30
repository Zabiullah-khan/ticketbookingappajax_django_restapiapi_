from django.shortcuts import render,HttpResponse
from .models import Passenger
from .serializers import Passengers_api
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.conf import settings
import ntplib
from datetime import datetime
import json
import os

# Create your views here.
flight_location = {'loc':'none',}


x=0
Total_seats=[]

def get_ntp_datetime():
    ntp_server = 'pool.ntp.org'

    try:
        client = ntplib.NTPClient()
        response = client.request(ntp_server)
        ntp_timestamp = response.tx_time
        ntp_datetime = datetime.fromtimestamp(ntp_timestamp)
        return ntp_datetime
        
    except Exception as e:
        print(f"Error fetching NTP time: {str(e)}")
        return None
current_datetime = get_ntp_datetime()
print(current_datetime.hour)

@csrf_exempt
def get_view(request):
	global x,file_location,Total_seats
	if request.method == 'GET':
	
		file_client = open('clients.json','r')
		for i in file_client:
			x+=1
		file_client.close()
	
		file_seats = open('seats.txt','r')
		for i in file_seats:
			if i not in Total_seats:
				Total_seats.append(i.replace('\n',''))
		file_seats.close()
		
		if current_datetime.hour < 10 or current_datetime.hour > 13  :
			flight_location['loc']='chennai'
		elif current_datetime.hour == 10 or current_datetime.hour ==13 :
			file_path = os.path.join(settings.BASE_DIR,'clients.json')
			file_path_seats = os.path.join(settings.BASE_DIR,'seats.txt')
			if os.path.exists(file_path) or os.path.exists(file_path_seats):
				os.remove(file_path)
				os.remove(file_path_exists)
				file_new = open('seats.txt','w')
				for i in range(1,21):
					file_new.write("Seat-TW-"+str(i))
				file_new.close()
					
		else:
			flight_location['loc']='delhi'
		
		print(flight_location)
		
		pass_data = {"seater":Total_seats,'locs':flight_location}
		
		return JsonResponse(pass_data,safe=False)

@csrf_exempt
@api_view(['POST'])
def post_view(request):
	global Total_seats
	
	if request.method == 'POST':
		serializer = Passengers_api(data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			st = serializer
			get_seat=st['seat_no'].value
			Total_seats=[]
			with open('seats.txt', 'r') as file:
				lines = file.readlines()
				print(lines)
				filtered_lines = [line for line in lines if str(get_seat+'\n') not in line]

			# Write the filtered lines back to the file
			with open('seats.txt', 'w') as file:
				file.writelines(filtered_lines)

			
			if current_datetime.hour !=10 and current_datetime.hour !=13:
				recod = open('clients.json','a')
				recod.write(json.dumps(serializer.data)+'\n')
				recod.close()
				msg={'mg':'done'}
				return JsonResponse(msg,safe=True)
			else:
				return JsonResponse({'closed_msg':'Tickets are Closed Try Later'})
			
		return JsonResponse(serializer.errors,status=400)
		
