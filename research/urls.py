from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('',include('pages.urls')),
    url('request/',include('equipmentrequests.urls')),
    path('equipments/',include('equipments.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('equipment-api/',include('equipments.api.urls','equipment-api')),
    path('request-api/',include('equipmentrequests.api.urls','request-api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
