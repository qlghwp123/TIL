from django.urls import path
from . import views

# URL namespace 지정
app_name = 'articles'

# 각 CRUD URL 에 mapping 되는 URL dispatcher 설정
urlpatterns = [
    path('create/', views.create, name='create'),
    path('index/', views.index, name='index'),
    path('<int:_id>/', views.detail, name='detail'),
    path('<int:_id>/update', views.update, name='update'),
    path('<int:_id>/delete', views.delete, name='delete'),
]