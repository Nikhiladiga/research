from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'),name='logout'), 
    path('display',views.display,name='display'),
]
