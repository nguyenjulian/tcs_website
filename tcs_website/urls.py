"""tcs_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin

from apps.home import views as home_views
from apps.portfolio import views as portfolio_views

urlpatterns = [
    # home urls
    url(r'^$', home_views.index),
    url(r'^home/$', home_views.index),

    # portfolio urls
    url(r'^portfolio/$', portfolio_views.index),
    url(r'^projects/', portfolio_views.projects),

    # admin urls
    url(r'^admin/', admin.site.urls)
]
