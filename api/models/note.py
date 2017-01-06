from django.db import models
#from django.contrib.contenttypes import *

#import api.lists.country_list
#import api.lists.store_list

class Note(models.Model):
    created             = models.DateTimeField(auto_now_add=True)
    #attached_to         = models.GenericForeignKey('content_type', 'object_id')
    body                = models.TextField()
    # user

    class Meta:
        ordering    = 'created'
        app_label   = 'api'
