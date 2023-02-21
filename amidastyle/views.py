import time

from django.db.migrations import serializer
from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from amidastyle.models import CustomUser, Advertisement, product
from amidastyle.serializers import UserSerializer, AdvertisementSerializer, ProductSerializer, SubscriptionSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    pagination_class = LimitOffsetPagination

    def get_user(self, request):
        account_id = self.kwargs['account_id']
        return product.objects.filter(account_id=account_id)


class UpdateUserSubscription(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'account_id'
    lookup_field = 'account_id'

    def get_serializer_class(self):
        if self.request.path.endswith('/subscription/'):
            return SubscriptionSerializer
        return super().get_serializer_class()


class AdvertisementViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    pagination_class = LimitOffsetPagination


class ProductUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = product.objects.all()
    pagination_class = LimitOffsetPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = product.objects.all()
    pagination_class = LimitOffsetPagination


class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        return product.objects.filter(account_id=account_id)


class AdvertisementList(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        return Advertisement.objects.filter(account_id=account_id)


@api_view(["GET"])
def health_check(request):
    time.sleep(1)
    return Response({"status": "Ok"}, status.HTTP_200_OK)


