from django.shortcuts import render, redirect
from .models import property,pslot,userProfile,bookingDetails,mark_pslot_unavailable,mark_pslot_available,reviewDetails,reportDetails
from django.contrib.auth.models import User, auth
from django.forms import ModelForm
from django.http import JsonResponse

# Create your views here.
class EditProperty(ModelForm):
	class Meta:
	    model = property
	    fields = ['img1','img2','img3']

def reportuser(request,id):
	print("haiii");
	ruser=User.objects.get(id=id)
	print(ruser)
	chkreport=reportDetails.objects.filter(userid=id)
	print(chkreport.count())
	if chkreport.count() < 3 :
		instance=reportDetails(userid=ruser,reportedby=request.user)
		instance.save()
		return JsonResponse({"instance": "Success"}, status=200)
	else:
		ruser=User.objects.get(id=id)
		ruser.is_active=False
		ruser.save()
		print("user bloked")
		return JsonResponse({"instance": "Success"}, status=200)


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

def editproperty(request):
	if request.method=='POST':
		try:
			isactive=request.POST['isactive']
			isactive=True
		except:
			isactive=False
		
		propertyid=request.POST['propertyid']
		name=request.POST['name']
		description=request.POST['description']
		mapurl=request.POST['mapurl']
		upi=request.POST['upi']
		place=request.POST['place']
		district=request.POST['district']
		try:
			img1=request.FILES['img1']
			
		except:
			img1=None
		try:
			img2=request.FILES['img2']
		except:
			img2=None
		try:
			img3=request.FILES['img3']
		except:
			img3=None

		results=property.objects.get(id=propertyid)
		results.name=name
		results.description=description
		results.mapurl=mapurl
		results.upi=upi
		results.place=place
		results.district=district
		if img1:
			results.img1=img1
		if img2:
			results.img2=img2
		if img3:
			results.img3=img3
		results.save()

		return redirect('/vpdetails/'+str(results.id))
	else:
		id=request.GET['id']
		results=property.objects.get(id=id)
		form = EditProperty(initial={'img1':results.img1,'img2':results.img2,'img3':results.img3})
		
		return render(request,'vendor/editproperty.html',{'results':results,'form':form})

def deleteproperty(request,id):
	results=property.objects.get(id=id)
	results.delete()
	return redirect('/slotmanage')

def addproperty(request):
	if request.method=='POST':
		try:
			isactive=request.POST['isactive']
			isactive=True
		except:
			isactive=False
		
		name=request.POST['name']
		description=request.POST['description']
		mapurl=request.POST['mapurl']
		upi=request.POST['upi']
		place=request.POST['place']
		district=request.POST['district']
		try:
			img1=request.FILES['img1']
			
		except:
			img1=None
		try:
			img2=request.FILES['img2']
		except:
			img2=None
		try:
			img3=request.FILES['img3']
		except:
			img3=None

		
		results=property.objects.create(name=name,description=description,mapurl=mapurl,upi=upi,place=place,district=district,img1=img1,img2=img2,img3=img3,owner=request.user)
		results.save()
		return redirect('/slotmanage')
	else:
		form = EditProperty()
		
		return render(request,'vendor/addproperty.html',{'form':form})

def vhistory(request):
	try:
		
		booklista=bookingDetails.objects.filter(pslotid__propertyid__owner=request.user,status=False).order_by('-id')
		booklistn=bookingDetails.objects.filter(pslotid__propertyid__owner=request.user,status=True).order_by('-id')
		print(booklista)
		print(booklistn)
	except:
		booklista=None
		booklistn=None
	return render(request,'vendor/vhistory.html',{'ahistory':booklista,'nhistory':booklistn})

def vabout(request):
	return render(request,'vendor/about.html')

def vsignup(request):
	if not request.user.is_anonymous:
		return redirect('/')
	if request.method == 'POST':
		Username=request.POST['Username']
		Password=request.POST['Password']
		Firstname=request.POST['Firstname']
		Lastname=request.POST['Lastname']
		Email=request.POST['Email']
		state=request.POST['state']
		house=request.POST['house']
		town=request.POST['town']
		pincode=request.POST['pincode']
		phone=request.POST['phone']
		try:
			user =User.objects.create_user(username=Username,first_name=Firstname,last_name=Lastname,email=Email,password=Password)
			userp=userProfile.objects.create(user=user,state=state,house=house,town=town,isvendor=True,pincode=pincode,phone=phone)
			user.save()
			userp.save()
			print('created')
		except Exception as e:
			if 'UNIQUE constraint' in str(e):
				return render(request,"vendor/signup.html",{'msg':"username/email already taken"})
			return render(request,"vendor/signup.html",{'msg':e})
		return render(request,"vendor/signup.html",{'msg':"Account created successfully"})
	else:
		return render(request,"vendor/signup.html")
