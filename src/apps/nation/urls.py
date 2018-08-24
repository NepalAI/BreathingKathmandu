from django.urls import path
from .views import HomePageView, ConservationPageView, district_data, instance_data, conservation_data, instance_conservation_data

app_name = 'city'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('conservation/', ConservationPageView.as_view(), name='conservation'),
    path('district_data/', district_data, name='district'),
    path('instance_data/', instance_data, name='instance'),
    path('conservation_data/', conservation_data, name='conservation'),
    path('instance_conservation_data/', instance_conservation_data, name='instance_conservation'),
]
