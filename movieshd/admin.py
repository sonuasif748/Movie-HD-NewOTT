from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(add_categories)
admin.site.register(customer)
admin.site.register(publisher)

# admin.site.register(PayHistory)
admin.site.register(Membership)
admin.site.register(UserMembership)
admin.site.register(Subscription)