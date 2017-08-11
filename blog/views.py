from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_home(request): #create
	return HttpResponse("<h1>Hello charul</h1>")
def blog_create(request): #create
	return HttpResponse("<h1>create</h1>")
def blog_detail(request): #retrieve
	return HttpResponse("<h1>detail</h1>")
def blog_list(request): #list items
	return HttpResponse("<h1>list</h1>")
def blog_update(request): #
	return HttpResponse("<h1>update</h1>")
def blog_delete(request):
	return HttpResponse("<h1>delete</h1>")				
def blog_template(request):	#template
	return render(request, "index.html", {})