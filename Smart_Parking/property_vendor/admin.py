from django.contrib import admin

# Register your models here.
from .models import property,pslot,userProfile,bookingDetails
# Register your models here.
admin.site.register(property)
admin.site.register(pslot)
admin.site.register(userProfile)
admin.site.register(bookingDetails)