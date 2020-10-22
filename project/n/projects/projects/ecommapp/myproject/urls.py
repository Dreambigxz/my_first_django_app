"""myproject URL Configuration

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
admin.autodiscover()
from django.conf.urls.static import static
from django.urls import path, include
from  django_email_verification import urls as mail_urls
from django.conf import settings




urlpatterns = [
    path('', include('users.urls')),
    path('', include('rapp.urls')),
    path('', include('ecommerce.urls')),
    path('', include('userwallet.urls')),
    path('admin/', admin.site.urls),
    path('email/', include(mail_urls)),
    path('', include('django.contrib.auth.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
