from django.urls import path, include
from . import views
from rest_framework import routers

# define router
router = routers.DefaultRouter()
router.register('schedules', views.ScheduleView)

urlpatterns = [
    path('', include(router.urls))
]
