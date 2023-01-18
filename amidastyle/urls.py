from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from amidastyle.views import (
    UserViewSet, health_check, AdvertisementViewSet, ProductViewSet, AdvertisementList,

)


router = DefaultRouter()
router.register(r'advertisement', AdvertisementViewSet)
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("ping/", health_check),
    re_path('^Advertisement/(?P<user_id>.+)/$', AdvertisementList.as_view()),
]
