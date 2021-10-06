from django.contrib import admin

from pyNKSapp.models import signupdetails,enrolled,staff_details
# Register your models here.

admin.site.register(signupdetails)
admin.site.register(enrolled)
admin.site.register(staff_details)