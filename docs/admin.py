from django.contrib import admin
from .models import *


admin.site.site_header = "Единое окно"
admin.site.site_title = "Единое окно"
admin.site.index_title = "Единое окно"

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'department', 'faculty',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'group')
    prepopulated_fields = {"slug": ("name",)}

class FacultiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'faculty')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'faculty')

class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'department')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'department')



admin.site.register(Faculties, FacultiesAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Obhodnoi)

