"""
URL configuration for ttpro project.

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
from django.urls import path
from triapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sing',views.host_signup,name="sing"),
    path('',views.host_login,name='login'),
    path('home',views.home_page ,name='home'),   
    # path('get_data/<email>/',views.get_data, name='get_data'),
    path('forgot_password', views.host_forgot_password, name='forgot_password'),
    path('change_password', views.host_change_password, name='change_password'),
]