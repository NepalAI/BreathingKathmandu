from django.urls import path
from .views import home

app_name = 'city'
urlpatterns = [
    path('', home, name='home')
]
