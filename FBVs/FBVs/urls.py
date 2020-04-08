"""FBVs URL Configuration

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
from django.conf.urls import url
from FBVsApp import views
from FBVsAccountApp import views2
from relationapp import views3
from middlewareapp import viewsm
urlpatterns = [
    url('admin/', admin.site.urls),
    url('show/',views.show_view),
    url('insert/',views.insert_view),
    url('update/(?P<id>\d+)/',views.update_view),
    url('delete/(?P<id>\d+)/',views.delete_view),
    url('index/',views.index_view),
    url('account/',views2.display_view),
    url('relation/',views3.display_view3),
    url('middlew/',viewsm.welcome_view),
    url('middleh/',viewsm.home_page_view),
    url('middlee/',viewsm.home_page_view2),
    url('middlefs/',viewsm.home_page_view3),
]
