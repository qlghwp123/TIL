from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_read, name='index'),
    path('create/', views.todo_create, name='create'),
    path('read/', views.todo_read, name='read'),
    path('update/<int:_id>', views.todo_update, name='update'),
    path('delete/<int:_id>', views.todo_delete, name='delete'),
]