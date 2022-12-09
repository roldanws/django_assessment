"""django_test URL Configuration

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
from django.urls import path, include
from django.contrib.auth import login
from customer.urls import customer_patterns
from administrator.urls import administrator_patterns
from .router import router
# Api router
#router = routers.DefaultRouter()
#router.register('films', film_views.FilmViewSet, basename='Film')
#router.register('genres', film_views.GenreViewSet, basename='FilmGenre')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(customer_patterns)),
    path('', include(administrator_patterns)),
    # Api routes
    path('api/', include('authentication.urls')),
    path('api/', include(router.urls), name = 'api'),
    #path('', include('administrator.urls',namespace="administrator")),
]