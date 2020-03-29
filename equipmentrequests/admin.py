from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import EquipmentRequest

class EquipmentRequestAdmin(ImportExportModelAdmin):
    list_display = ('id','name','eqpname','department','request_status','fromDate','toDate')
    list_display_links=('id','name')
    list_filter = ('name','eqpname','request_status','department')
    search_fields=('name','id','eqpname')
    list_editable=('request_status',)
    list_per_page=25

admin.site.register(EquipmentRequest,EquipmentRequestAdmin)
