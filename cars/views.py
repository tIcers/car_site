from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.

def list(request):
	return render(request, 'car/list.html')

def add(request):
	return render(request, 'car/add.html')

def delete(request):
	return render(request, 'car/delete.html')