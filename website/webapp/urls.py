"""website URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page, name = "landing_page"),
    path('studymat/',views.studymat, name = "study_materials"),
    path('scholarships/',views.scholarships, name="scholarships"),
    path('buycourse/',views.buycourse,name="buycourse"),
    path('about/', views.about, name="about"),
    path('career/',views.career, name="career"),
    path('child/',views.child,name="child"),
    path('privacy/',views.privacy,name="privacy"),
    path('termscondition/',views.termscondition,name="termscondition"),
    path('contact/',views.contact,name="contact"),
]
