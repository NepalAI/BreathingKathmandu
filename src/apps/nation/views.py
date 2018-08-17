from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize

from .models import Instance, Nepal


class HomePageView(TemplateView):
	template_name = 'interface/index.html'


def district_data(request):
	districts = serialize('geojson', Nepal.objects.all())
	return HttpResponse(districts, content_type='json')


def instance_data(request):
	pass