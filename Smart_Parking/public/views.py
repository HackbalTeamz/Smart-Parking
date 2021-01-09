from django.shortcuts import render, redirect
from property_vendor.models import property,pslot,userProfile
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
	return render(request,'public/index.html')

def search(request):
	results=property.objects.all()
	return render(request,'public/search.html',{'results':results})

def pdetails(request,id):
	result=property.objects.get(id=id)
	return render(request,'public/single.html',{'property':result})

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