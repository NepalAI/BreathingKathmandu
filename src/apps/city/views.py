from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
	context = {
	'page_title': 'Home'
	}
	return render(request, 'interface/index.html', context)