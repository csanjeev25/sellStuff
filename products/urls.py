"""sellStuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import (ProductListView,
    productListView,
    ProductDetailView,
    productDetailView, 
    ProductFeaturedListView, 
    ProductDetailSlugView,
    ProductFeaturedDetailView)

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^-fbv/$', productListView),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^-fbv/(?P<pk>\d+)/$', productDetailView),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]

