from django.contrib import admin

# Register your models here.
from goods.models import Catigories, Projects

# admin.site.register(Catigories)
# admin.site.register(Projects)




@admin.register(Catigories)
class CatigoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}




@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}


