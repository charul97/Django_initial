from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
#from rest_framework import viewsets
from blog.models import Post
from blog.forms import PostForm
#from blog.serializers import PostSerializers
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
#def blog_home(request): #create
#	return HttpResponse("<h1>Hello charul</h1>")


def blog_create(request): #create
	form=PostForm(request.POST or None)
	if request.method=="POST":
		print (request.POST.get("author")) #to print the values of author, title and text in terminal
		print (request.POST.get("title"))
		print (request.POST.get("text"))
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()	
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"There was some error in creating")	
	context={
		"form":form,
	}
	return render(request, "post_form.html", context)


def blog_detail(request, id=None): #retrieve
	instance=get_object_or_404(Post, id=id)
	context={
		"title":instance.title,
		"instance":instance,
	}
	return render(request, "post_detail.html", context)


def blog_list(request): #list items
	queryset=Post.objects.all()
	context={
		"object_list":queryset,
		"title":"List"
	}
	return render(request, "base.html", context)


def blog_update(request, id=None): #
	instance=get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()	
		messages.success(request,"Successfully Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"title":instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)



def blog_delete(request, id=None):
	instance=get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Successfully deleted")
	return redirect("blog:list")

#def blog_template(request):	#template
#	if request.user.is_authenticated():
#		context={
#			"title":"user is authenticated"
#		}
#	else:
#		context={
#		"title":"hi this is context also here"
#	}


#	return render(request, "index.html", context)


#class PostSet(viewsets.ModelViewSet):
#	queryset=Post.objects.all()
#	serializer_class=PostSerializers