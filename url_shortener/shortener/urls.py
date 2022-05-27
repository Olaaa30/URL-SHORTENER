from django.urls import path
from shortener import views

urlpatterns = [
  path('', views.index, name='index'),
  path('create', views.create, name='create' ),
  path('<str:pk>', views.go, name='create' ),
]