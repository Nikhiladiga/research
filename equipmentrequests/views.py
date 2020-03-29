from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .models import EquipmentRequest


@login_required
def request(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        designation = request.POST['designation']
        eqpname = request.POST['eqpname']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']
        message = request.POST['message']
        user_id = request.POST['user_id']

        equipmentrequest = EquipmentRequest(name=name, department=department,designation=designation,eqpname=eqpname,fromDate=fromDate,toDate=toDate,message=message,user_id=user_id)

        equipmentrequest.save()

        messages.success(request,'Your request has been successfully submitted!')
        return redirect('/equipments');
    return render(request,'equipmentrequests/request.html')



