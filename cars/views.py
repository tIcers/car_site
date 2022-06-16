from django.shortcuts import render

# Create your views here.
def list(request):
	return render(request,'cars/list.html')

def add(request):
	return render(request,'cars/add.html')
	
def delete(request):
	return render(request,'cars/delete.html')