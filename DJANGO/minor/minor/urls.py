"""minor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
=======
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
>>>>>>> 86824304de2580eeee05b3472a6bea444bc535d1
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
<<<<<<< HEAD
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls'))
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> 86824304de2580eeee05b3472a6bea444bc535d1
