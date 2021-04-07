from django.shortcuts import render, redirect
from .models import property,pslot,userProfile,bookingDetails,mark_pslot_unavailable,mark_pslot_available,reviewDetails
from django.contrib.auth.models import User, auth

# Create your views here.
def slotmanage(request):

	results=property.objects.filter(owner=request.user)
	print(results)
	return render(request,'vendor/dashboard.html',{'pbooks':results})

def vpdetails(request,id):
	isfw=False
	istw=False
	isroofed=False
	isfenced=False
	isavailable=False
	buyed=False
	result=property.objects.get(id=id)
	plotresult=pslot.objects.filter(propertyid=id)
	for plot in plotresult:
		if plot.isfw:
			isfw=True
		if plot.istw:
			istw=True
		if plot.isroofed:
			isroofed=True
		if plot.isfenced:
			isfenced=True
		if plot.isavailable:
			isavailable=True

	try:
		chkreview=reviewDetails.objects.filter(propertyid=result)
	except reviewDetails.DoesNotExist:
		chkreview=None

	return render(request,'vendor/single.html',{'chkreview':chkreview,'pslots':plotresult,'property':result,'isavailable':isavailable,'istw':istw,'isfw':isfw,'isfenced':isfenced,'isroofed':isroofed})

def deleteslot(request,id):
	results=pslot.objects.get(id=id)
	pid=results.propertyid.id
	results.delete()
	return redirect('/vpdetails/'+str(pid))

def addslot(request):
	if request.method=='POST':
		propertyid=request.POST['propertyid']
		try:
			isfw=request.POST['isfw']
			isfw=True
		except:
			isfw=False
		try:
			istw=request.POST['istw']
			istw=True
		except:
			istw=False
		try:
			isroofed=request.POST['isroofed']
			isroofed=True
		except:
			isroofed=False
		try:
			isfenced=request.POST['isfenced']
			isfenced=True
		except:
			isfenced=False
		rate=request.POST['rate']
		results=property.objects.get(id=propertyid)
		instance=pslot(propertyid=results,isfw=isfw,istw=istw,isroofed=isroofed,isfenced=isfenced,rate=rate)
		instance.save()

		return redirect('/vpdetails/'+str(results.id))
	else:
		id=request.GET['id']
		results=property.objects.get(id=id)
		return render(request,'vendor/addslot.html',{"results":results})

def editslot(request):
	if request.method=='POST':
		pslotid=request.POST['pslotid']
		try:
			isfw=request.POST['isfw']
			isfw=True
		except:
			isfw=False
		try:
			istw=request.POST['istw']
			istw=True
		except:
			istw=False
		try:
			isroofed=request.POST['isroofed']
			isroofed=True
		except:
			isroofed=False
		try:
			isfenced=request.POST['isfenced']
			isfenced=True
		except:
			isfenced=False
		rate=request.POST['rate']
		results=pslot.objects.get(id=pslotid)
		results.isfw=isfw
		results.istw=istw
		results.isroofed=isroofed
		results.isfenced=isfenced
		results.rate=rate
		results.save()

		return redirect('/vpdetails/'+str(results.propertyid.id))
	else:
		id=request.GET['id']
		results=pslot.objects.get(id=id)
		return render(request,'vendor/editslot.html',{"results":results})
