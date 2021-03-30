from django.urls import path, include
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<int:book_id>/', views.detail, name="detail")
] 
