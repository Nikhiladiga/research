from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Equipment

class EquipmentAdmin(ImportExportModelAdmin):
    list_display = ('id','Equipment_Name','Incharge_ID','Status','image_main')
    list_display_links = ('id','Equipment_Name')
    list_filter = ('Status',)
    search_fields = ('id','Equipment_Name','Status','Incharge_ID','Product_ID')
    list_per_page = 25


admin.site.register(Equipment, EquipmentAdmin)
