"""DataCenter URL Configuration

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
from django.contrib import admin
from django.http import HttpResponse

def funtemp(request):
	return HttpResponse("<body bgcolor=pink><font color=red align=center> <h1> Weather Report <h1></font><br><h2>Todays Temperature is: 27.56</h2> </body>")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_temp/', funtemp),
]
