from django.urls import path, include
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]

