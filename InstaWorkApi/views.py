from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse
from InstaWorkApi.models import TeamMembers
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
	mainList = []
	total_list = list(TeamMembers.objects.all())
	print(len(total_list))
	for i in range(0, len(total_list)):
		newObject = {}
		newObject['first_name'] = total_list[i].first_name
		newObject['last_name'] = total_list[i].last_name
		newObject['phone_number'] = total_list[i].phone_number
		newObject['email'] = total_list[i].email
		newObject['role'] = total_list[i].role
		mainList.append(newObject)
	return JsonResponse({'list': mainList})

@csrf_exempt
def add_team_member(request):
	if request.method == 'POST':
		newRow = json.loads(request.body)
		try:
			tableRow = TeamMembers(first_name = newRow['first_name'], last_name=newRow["last_name"], phone_number=newRow["phone_number"],
						email=newRow['email'], role=newRow['role'])
		except:
			return HttpResponse('All fields should be specified')
		tableRow.save()
		total_list = list(TeamMembers.objects.all())
		
		newRow["id"] = tableRow.id
		return JsonResponse({'data':newRow})
	
	else:
		return HttpResponse('It is Post request')

@csrf_exempt
def edit_team_member(request):
	if request.method == 'POST':
		newRow = json.loads(request.body)
		id = int(newRow['id'])

		TeamMembers.objects.filter(id=id).update(**newRow)

		instance = TeamMembers.objects.get(id=id)
		newObject = {}
		newObject['id'] = instance.id
		newObject['first_name'] = instance.first_name
		newObject['last_name'] = instance.last_name
		newObject['phone_number'] = instance.phone_number
		newObject['email'] = instance.email
		newObject['role'] = instance.role

		return JsonResponse({'data':newObject})
	
	else:
		return HttpResponse('It is Post request')

@csrf_exempt
def delet_team_memeber(request):
	if request.method == 'GET':
		id = request.GET.get('id', None)
		instance = TeamMembers.objects.get(id=id)
		instance.delete()
		return JsonResponse({})
	else:
		return HttpResponse('It is GET request')
