from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello World! It`s polls index.")

def webtest(request):
	return HttpResponse("It`s webtest page.")

def Inetest(request):
	return HttpResponse("It`s Inetest page.")

