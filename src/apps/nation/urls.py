from django.urls import path
from .views import HomePageView, district_data, instance_data

app_name = 'city'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('district_data/', district_data, name='district'),
    path('instance_data/', instance_data, name='instance')
]
