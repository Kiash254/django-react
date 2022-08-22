from django.urls import path
from . import views

app_name='api'

urlpatterns = [
    path('todoview/',views.Todoview, name='todoview'),
    path('tododetail/<int:pk>/',views.TodoDetail, name='tododetail'),
    path('todocreate/',views.TodoCreate, name='todocreate'),
    path('todoupdate/<int:pk>/',views.TodoUpdate, name='todoupdate'),
    path('tododelete/<int:pk>/',views.TodoDelete, name='tododelete'),
]