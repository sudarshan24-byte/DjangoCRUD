from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('add-data', add_data),
    path('delete-data/<int:id>/', delete_data),
    path('update-data/<int:id>/', update_data),
    path('update-player/<int:id>/', update_player),
]