from django.urls import path, include
from . import views

app_name = 'move'

urlpatterns = [
    path('', views.all_moves, name='all_moves'),
    path('<int:move_id>/', views.detail, name="detail")
]
