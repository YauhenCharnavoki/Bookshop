from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.cart, name = 'cart'),
    path('<int:id>/add/', views.add, name = 'add'),
    path('<int:id>/remove/', views.remove, name = 'remove'),
    path('<int:id>/update/', views.update, name = 'update'),
    path('buy/', views.buy, name = 'buy'),
    path('clear/', views.clear, name = 'clear'),
]