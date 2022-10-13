from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/view', views.BookListView.as_view()),

]
