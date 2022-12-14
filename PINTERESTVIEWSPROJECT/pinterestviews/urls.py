"""pinterestviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pinterest import views as pinterestViews
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pinterestViews.home, name='home'),
    path('about/', pinterestViews.about, name='about'),
    path('signup/', pinterestViews.signup, name='signup'),
    path('news/', include('news.urls')),
    path('pinterest/', include('pinterest.urls')),
    path('accounts/', include('accounts.urls')),
    path('post/', pinterestViews.post, name='post'),
    path('author/', pinterestViews.author, name='author'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
