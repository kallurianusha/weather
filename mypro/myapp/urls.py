from .import views
from django.urls import path
urlpatterns = [
    path('weather/',views.weather),
]
