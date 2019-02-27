from django.urls import path, include
from . import views
from rest_framework import routers

# define router
router = routers.DefaultRouter()
router.register('vehicle_orders', views.VehicleOrderView)

urlpatterns = [
    path('', include(router.urls))
]
