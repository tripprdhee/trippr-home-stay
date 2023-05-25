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
# from django.urls import path
# from triapp import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('singup',views.host_signup,name="sing"),
#     path('login',views.host_login,name='login'),
#     path('home',views.home_page ,name='home'),   
#     # path('get_data/<email>/',views.get_data, name='get_data'),
#     path('forgot_password', views.host_forgot_password, name='forgot_password'),
#     path('change_password', views.host_change_password, name='change_password'),
# ]
from django.urls import path
from triapp.views import HostSignupView, HostLogView, HostForgotPasswordView, HostChangePasswordView,SearchResultsView,AllPropertiesView
from triapp.views import get_property_data,home_page,showSome
urlpatterns = [
    path('admin/', admin.site.urls),
    path('host_signup/', HostSignupView.as_view(), name='host_signup'),
    path('host_login/', HostLogView.as_view(), name='host_login'),
    path('host_forgot_password/', HostForgotPasswordView.as_view(), name='host_forgot_password'),
    path('host_change_password/', HostChangePasswordView.as_view(), name='host_change_password'),
    # path('home/', HomePageView.as_view(), name='home/'),
    path('home/',home_page),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('fetch_all/', AllPropertiesView.as_view(), name='all_properties'),
    path('property-data/', get_property_data, name='property_data'),
    path('some',showSome)
]   

