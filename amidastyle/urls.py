from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from amidastyle.views import (
    UserViewSet, health_check, AdvertisementViewSet, ProductViewSet, AdvertisementList,
    ProductView,  ProductUpdate, UpdateUserSubscription

)


router = DefaultRouter()
router.register(r'advertisement', AdvertisementViewSet)
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("ping/", health_check),
    path("products/<int:pk>/", ProductUpdate.as_view()),
    path("user/<int:account_id>", UpdateUserSubscription.as_view(), name='account-detail'),
    path('user/<int:account_id>/subscription/', UpdateUserSubscription.as_view(), name='account-subscription'),
    re_path('^Advertisement/(?P<account_id>.+)/$', AdvertisementList.as_view()),
    re_path('^Products/(?P<account_id>.+)/$', ProductView.as_view()),


]
