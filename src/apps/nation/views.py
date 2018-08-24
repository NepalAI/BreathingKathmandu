from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize

from .models import Instance, Nepal, InstanceConservation, Conservation


class HomePageView(TemplateView):
	template_name = 'interface/index.html'


class ConservationPageView(TemplateView):
	template_name = 'interface/conservation.html'


def district_data(request):
	districts = serialize('geojson', Nepal.objects.all())
	return HttpResponse(districts, content_type='json')


def instance_data(request):
	instances = serialize('geojson', Instance.objects.all())
	return HttpResponse(instances, content_type='json')


def conservation_data(request):
	conservations = serialize('geojson', Conservation.objects.all())
	return HttpResponse(conservations, content_type='json')


def instance_conservation_data(request):
	conservation_instances = serialize('geojson', InstanceConservation.objects.all())
	return HttpResponse(conservation_instances, content_type='json')