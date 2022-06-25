"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

#from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pybo/', views.index), ##pybo/ URL이 요청되면 views.index를 호출하라
    path('pybo/', include('pybo.urls')),
    #위에서 아래로 이동 config로 갈 필요 없이 pybo app 하위 파일에서 진행
]
