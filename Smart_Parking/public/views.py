from django.shortcuts import render, redirect
from property_vendor.models import property,pslot,userProfile
from django.contrib.auth.models import User, auth
from django.db.models import Q

# Create your views here.
def index(request):
	return render(request,'public/index.html')

def search(request):
	
	try:
		place = request.GET['place']
		vtype = int(request.GET['type'])
	except:
		vtype = 'All'
		place = ""	
	lookups= Q(propertyid__place__icontains=place) | Q(propertyid__district__icontains=place)
	if vtype==2:
		pslots=pslot.objects.values_list('propertyid',flat=True).filter(lookups,istw=True,isavailable=True).distinct()
		print(pslots)
		results=property.objects.filter(id__in=pslots)
		return render(request,'public/search.html',{'results':results})
	else:
		pslots=pslot.objects.values_list('propertyid',flat=True).filter(lookups,isfw=True,isavailable=True).distinct()
		results=property.objects.filter(id__in=pslots)
		return render(request,'public/search.html',{'results':results})

def pdetails(request,id):
	isfw=False
	istw=False
	isroofed=False
	isfenced=False
	isavailable=False

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

			



	return render(request,'public/single.html',{'pslots':plotresult,'property':result,'isavailable':isavailable,'istw':istw,'isfw':isfw,'isfenced':isfenced,'isroofed':isroofed})

def logout(request):
	if request.user.is_anonymous:
		return redirect('/')
	auth.logout(request)
	return redirect('/')

def login(request):
	if not request.user.is_anonymous:
		return redirect('/')
	if request.method == 'POST':
		password=request.POST['password']
		username=request.POST['username']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else :
			
			return render(request,"public/login.html",{'status':True})
	else:
		return render(request,"public/login.html")