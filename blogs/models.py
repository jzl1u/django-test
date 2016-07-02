from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class BlogPost(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	blog_title = models.CharField(max_length=20)
	blog_text = models.TextField()
	pub_date = models.DateTimeField('date published')


