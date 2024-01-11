from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls
# from django_otp.admin import OTPAdminSite
#
# admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('accounts/', include(tf_urls)),
    path('users/', include('users.urls')),
]