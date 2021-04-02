from django.contrib import admin
from django.urls import path, include
from To_Do_List import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('add_todo_list/', views.add_todo, name='todolist'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]