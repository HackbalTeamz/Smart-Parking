"""Smart_Parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from public import views as pv
from property_vendor import views as vv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pv.index,name="index"),
    path('search',pv.search,name="search"),
    path('pdetails/<int:id>',pv.pdetails,name="pdetails"),
    path('login',pv.login,name="login"),
    path('logout',pv.logout,name="logout"),
    path('booking/<int:id>',pv.booking,name="booking"),
    path('dashboard',pv.dashboard,name="dashboard"),
    path('checkout/<int:id>',pv.checkout,name="checkout"),
    path('payment/<int:id>',pv.payment,name="payment"),
    path('addreview', pv.addreview,name='add_review'),
    path('uhistory', pv.uhistory,name='uhistory'),
    path('slotmanage', vv.slotmanage,name='slotmanage'),
    path('vpdetails/<int:id>',vv.vpdetails,name="vpdetails"),
    path('deleteslot/<int:id>',vv.deleteslot,name="deleteslot"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
