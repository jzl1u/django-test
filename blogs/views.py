from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import BlogPost
from django.contrib.auth.models import User
from .forms import AddForm
# Create your views here.
def index(request):
	blog_list = BlogPost.objects.order_by('-pub_date')
	return render(request,"blogs/index.html",{'blog_list':blog_list})

def user(request,user_name):
	if request.method == 'POST':
		blog_info = AddForm(request.POST)
		if blog_info.is_valid():
			blog_to_add = BlogPost(user=User.objects.get(username=user_name),
			blog_title=blog_info.cleaned_data['title'],
			blog_text=blog_info.cleaned_data['text'],
			pub_date=blog_info.cleaned_data['date'])

			blog_to_add.save()
	blog_info = AddForm()
	blog_list = BlogPost.objects.filter(user=User.objects.filter(username=user_name))
	return render(request, 'blogs/user.html',{'form':blog_info,'blog_list':blog_list,'user_name':user_name})

def detail(request,blog_id):
	blogdetail=BlogPost.objects.get(id=blog_id)
	blog_info=AddForm(initial={
		'title':blogdetail.blog_title,
		'date':blogdetail.pub_date,
		'text':blogdetail.blog_text
	})
	if request.method == 'POST':
		if request.POST.has_key("remove"):
			blogdetail.delete()
			blog_info=AddForm()
			blog_list=BlogPost.objects.filter(user=User.objects.filter(username=blogdetail.user))
			
		if request.POST.has_key("modify"):
			blog_info = AddForm(request.POST)
			if blog_info.is_valid():
				blog_to_add = BlogPost.objects.get(id=blog_id)
				blog_to_add.blog_title=blog_info.cleaned_data['title']
				blog_to_add.blog_text=blog_info.cleaned_data['text']
				blog_to_add.pub_date=blog_info.cleaned_data['date']
				blog_to_add.save()

		return HttpResponseRedirect('/blogs/user/'+blogdetail.user.username)
	return render(request, 'blogs/detail.html',{
		'form':blog_info
	})
