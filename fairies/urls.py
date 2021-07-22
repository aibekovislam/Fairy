from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('sign-in/', sign_in, name="sign-in"),
    path('register', register, name="register")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
