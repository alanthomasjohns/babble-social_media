"""core URL Configuration

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
from django.urls import path, include
from accounts.views import *
from django.views.generic import TemplateView
from tweets.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name = "accounts/accounts.html")),
    path('register/', send_otp),
    path('verify_otp/', verify_otp),
    path('login/', login_user),
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('tweets/<int:tweet_id>', tweet_detail_view),
    path('tweets/', tweet_list_view),

    path('accounts/', include('allauth.urls')),

    path('api-auth/', include('rest_framework.urls')),
]
