from . import views
from django.urls import path

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('delete/<int:activity_id>/', views.remove_activity, name='delete'),
]
