from django.shortcuts import render, redirect
from property_vendor.models import property,pslot,userProfile
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
	return render(request,'public/index.html')

def search(request):
	'''try:
		place = request.GET['place']
		vtype = request.GET['type']
	except:
		vtype = 'All'
		place = ""	

		All1=products.objects.filter(isactive=True,pname__icontains=name,owner__userprofile__pincode__range=[int(request.user.userprofile.pincode)-2,int(request.user.userprofile.pincode)+2]).order_by('id')

	return render(request, 'public/shop.html',{'All':All,'Vegetables':Vegetables,'Fruits':Fruits,'Products':Product,'Dried':Dried,'cat':cat})
'''
	results=property.objects.all()
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

			



	return render(request,'public/single.html',{'property':result,'isavailable':isavailable,'istw':istw,'isfw':isfw,'isfenced':isfenced,'isroofed':isroofed})

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