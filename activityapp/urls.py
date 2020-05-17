from django.urls import include, path
from rest_framework import routers
from .views import ActivityViewSet

router = routers.DefaultRouter()
router.register(r'users/activites', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]