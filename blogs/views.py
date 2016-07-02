from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	blog_list = BlogPost.objects.order_by('-pub_date')
	return render(request,"blogs/index.html",{'blog_list':blog_list})

def user(request,user_name):
	blog_list = BlogPost.objects.filter(user=User.objects.filter(username=user_name))
	return HttpResponse("User")
