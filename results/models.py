from django.db import models
from datetime import *

from django.contrib.auth.models import User
#
# class personal_info(models.Model):
#
# 	firstname = models.CharField(max_length=50, blank = True, null = True)
# 	lastname = models.DecimalField(max_length=30, decimal_places=3, max_digits=8, blank = True, null = True)
# 	address = models.CharField(max_length=300, blank = True, null = True)
# 	zipcode = models.CharField(max_length=300, blank = True, null = True)
# 	City =  models.CharField(max_length=300, blank = True, null = True)
# 	#radio button for beginner starting set
#

class articles(models.Model):

	titlea = models.CharField(max_length=3000, blank = True, null = True)
	message = models.TextField(blank = True, null = True)
	picture =  models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
	date_created = models.DateTimeField(default=datetime.now())
	google_doc_link = models.CharField(max_length=3000, blank = True, null = True)
