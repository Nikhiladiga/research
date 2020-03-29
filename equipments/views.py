from django.shortcuts import render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required

from .models import Equipment

@login_required
def index(request):
    equipments = Equipment.objects.all()
    paginator = Paginator(equipments,6)
    page= request.GET.get('page')
    paged_equipments = paginator.get_page(page)

    context = {
        'equipments':paged_equipments
    }
    return render(request,'equipments/index.html',context)

