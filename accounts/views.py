from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from equipmentrequests.models import EquipmentRequest

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check username
        if User.objects.filter(username = username).exists():
            messages.error(request,'Username is taken')
            return redirect('register')
        else:
            if User.objects.filter(email = email).exists():
                messages.error(request,'Email already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name = first_name, last_name = last_name)
                user.is_active = False
                user.save()
                auth.login(request,user)
                messages.success(request,'Successfully registered')
                return redirect('home')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('home')

        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')

def display(request):
    user_requests = EquipmentRequest.objects.filter(user_id=request.user.id)

    context = {
        'requests': user_requests
    }
    return render (request, 'accounts/requests.html',context)