from django.urls import path, include
from . import views
from rest_framework import routers

# define router
router = routers.DefaultRouter()
router.register('workcenters', views.WorkCenterView)

urlpatterns = [
    path('', include(router.urls))
]
