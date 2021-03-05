"""ten_k_brews URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # browse urls
    path('browse/all', views.browse_all, name='all'),
    path('browse/breweries', views.browse_breweries, name='breweries'),
    path('browse/wineries', views.browse_wineries, name='wineries'),
    path('browse/distilleries', views.browse_distilleries, name='distilleries'),
    path('browse/cideries', views.browse_cideries, name='cideries'),

    # detail page urls
    path('establishment/<int:establishment_pk>', views.establishment_detail, name='establishment_detail'),
    path('drink/<int:drink_pk>', views.drink_detail, name='drink_detail'),

    # form urls
    path('new_drink/<int:establishment_pk>', views.new_drink_form, name='new_drink_form')
]
