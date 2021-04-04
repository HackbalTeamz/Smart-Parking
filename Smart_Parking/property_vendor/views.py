from django.shortcuts import render
from .models import property,pslot,userProfile,bookingDetails,mark_pslot_unavailable,mark_pslot_available,reviewDetails
from django.contrib.auth.models import User, auth

# Create your views here.
def slotmanage(request):

	results=property.objects.filter(owner=request.user)
	print(results)
	return render(request,'vendor/dashboard.html',{'pbooks':results})

