"""
URL configuration for TransitInsights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from FirstApp.views import *
from django.conf import settings
from django.conf.urls.static import static

appname = "First_App"

urlpatterns = [
    path('', Start_Page, name='Start_Page'),
    path('Second_Page/<str:sw_id>/', Second_Page, name='Second_Page'),
    path('Third_Page/', Third_Page, name='Third_Page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)