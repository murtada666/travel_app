"""config URL Configuration

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

from django.conf.urls import include
from ninja import NinjaAPI


from travel.api.trip import trip_router
from travel.api.booking import booking_router
from travel.api.city import city_router
from travel.api.country import country_router
from travel.api.agency import agency_router
from travel.api.destination import destination_router


api = NinjaAPI()

api.add_router("/trip_router", trip_router)
api.add_router("/booking_router", booking_router)
api.add_router("/city_router", city_router)
api.add_router("/country_router", country_router)
api.add_router("/agency_router", agency_router)
api.add_router("/destination_router", destination_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path('accounts/', include('allauth.urls')),
]
