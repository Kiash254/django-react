from django.contrib import admin
from .models import Todo
# Register your models here.



admin.site.site_header = 'Todo App'
admin.site.site_title = 'Todo App'
admin.site.index_title = 'Todo App'
admin.site.register(Todo)
