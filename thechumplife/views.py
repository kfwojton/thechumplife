
#django var for upload test
from json import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



global account_form
from zipcode_dict import *
from django.contrib.sessions.backends.db import *
from django.shortcuts import render
from django.contrib.auth.models import *
from django.contrib.auth import authenticate,login, logout
from forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import sys
from django import forms
from django.contrib.auth.models import User
from re import *
import string
import random
from forms import *
from forms import gather_emailq
from finder import *
from checknullvar import *
from results.models import *

from random import randint
from datetime import *
from django.contrib.auth.models import User
from math import *
from django.core.mail import EmailMessage


#django var for upload test

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


#end of django var for upload test

sys.path.append('/user/kevinwojton/Hack/hub3')
sys.path.append('/user/kevinwojton/Hack/hub3/results')


from results.models import *


from forms import *
from unicodedata import *







def start(request):

    gather_emaila = gather_emailq()
    ko = articles.objects.all()


    if 'gather_email' in request.POST:
        if gather_email.is_valid():
            print "subscription email recieved"
            firstnamea = gather_emailb.cleaned_data['firstname']

            ko = user_emails(email = firstnamea)
            ko.save()

    k =  articles.objects.all()


    number_of_articles = len(k)
    return render(request, "index.html", {'gather_email':gather_emaila, 'data':k,'datab':ko,'number_of_articles':number_of_articles})



def article(request, name):

    print '[name]'
    print name
    k = articles.objects.get(id = int(name))
    ko = articles.objects.all()

    print k


    nexta = articles.objects.filter(id = k.id + 1)
    previous = articles.objects.filter(id = k.id - 1)


    op = articles.objects.all()
    if len(nexta)<> 0 :
        nexta = nexta[0].id

    if len(previous)<> 0 :
        previous = previous[0].id
    number_of_articles = len(ko)
    return render(request, 'article.html', {'number_of_articles':number_of_articles,'datac': k,'datab':ko, 'nexta':nexta, 'previous':previous, 'articles':op})

def auto(request,name):

    html = name + '.html'

    return render(request, html)
