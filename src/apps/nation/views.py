from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'interface/index.html'