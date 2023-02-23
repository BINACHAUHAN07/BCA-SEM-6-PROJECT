from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(user)
admin.site.register(contact)
admin.site.register(feedback)
admin.site.register(booking)
admin.site.register(comment)