from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Mander)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(Request)
admin.site.register(RequestManager)
admin.site.register(Document)
admin.site.register(Vehicle)