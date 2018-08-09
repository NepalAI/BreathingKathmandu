from django.urls import path
from .views import home

app_name = 'interface'
urlpatterns = [
    path('', home, name='home')
]