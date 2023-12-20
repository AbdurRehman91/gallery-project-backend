from django.urls import path
from .views import pictures, save_picture

urlpatterns = [
    path('api/pictures/', pictures, name='pictures-list'),
    path('api/save_picture/', save_picture, name='new-picture'),
]