from django.urls import path, include
from . import views
from rest_framework import routers

# define router
router = routers.DefaultRouter()
router.register('vehicle_components', views.VehicleComponentView)

urlpatterns = [
    path('', include(router.urls)),
]
