from django.contrib import admin
from .models import TaskModel

class TaskAdmin(admin.ModelAdmin):
    list_display=['task','date','complete']
    #list_editable=['date','complete']
    list_per_page=4

admin.site.register(TaskModel,TaskAdmin)
# Register your models here
