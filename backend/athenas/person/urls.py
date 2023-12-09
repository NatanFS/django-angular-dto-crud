

from django.urls import path, include
from rest_framework import routers
from person.viewsets import PersonViewSet

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
urlpatterns = [
     path("", include((router.urls, 'person'), namespace='person_urls')),
]
