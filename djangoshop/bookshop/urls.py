from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.index, name = 'catalog'),
    path('<int:id>/view/', views.book, name = 'view'),
]