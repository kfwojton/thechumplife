from django.contrib import admin
from results.models import *
from models import *
# Register your models here.
# admin.site.register(articles)

#admin.site.register(initialquestion)
from django.forms import TextInput, Textarea
from django.db import models



class kevin(admin.ModelAdmin):
    formfield_overrides = {
    
        models.CharField: {'widget': Textarea(attrs={'rows':10, 'cols':40})},
    }


admin.site.register(articles, kevin)
