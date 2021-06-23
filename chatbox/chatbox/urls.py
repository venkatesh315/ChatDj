"""chatbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from mychat.views import welcome
from mychat import views as v



urlpatterns = [
    path('admin/', admin.site.urls),                       #superuser
    path('home',welcome,name='home-wel'),                                   #home page
    path("register/", v.register, name="register"),        #signup
    path('captcha/', include('captcha.urls')),            #captcha
    path('', include("django.contrib.auth.urls")),         #login and logout
    path('profile/', v.view_profile, name='view_profile'),
    path('profile/edit/', v.edit_profile, name='edit_profile'),
    path('profile/password/', v.change_password, name='change_password'),
    path('profile/others', v.search_option, name='search'),

]
