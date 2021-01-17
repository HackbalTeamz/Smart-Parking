from django.contrib import admin

# Register your models here.
from .models import property,pslot,userProfile,bookingDetails,reviewDetails
# Register your models here.
admin.site.register(property)
admin.site.register(pslot)
admin.site.register(userProfile)
admin.site.register(bookingDetails)
admin.site.register(reviewDetails)