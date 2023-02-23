"""tour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from .import views
from login import urls
from django.conf import settings
from package import urls
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('acount',include('login.urls')),
    path('logout/',include('login.urls')),
    path('about/',views.about),
    path('forget',views.forget),
    path('service/',views.service),
    path('contact/',views.contact1),
    path('feedback/',views.feedback1),
    path('tourpackage/',include('package.urls')),
    path('destination/',views.destination),
    path('travelguide/',views.travelguide),
    path('booking/',views.booking1),
    # path('bloggrid/',views.bloggrid),
    path('bookingstatus/',views.bookingstatus),
    path('packagedetails/',views.packagedetails),
    path('profile/',views.profile),
    path('comment/',views.comment1),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    