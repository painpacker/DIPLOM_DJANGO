import time
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from amidastyle.models import CustomUser, Advertisement, product
from amidastyle.serializers import UserSerializer, AdvertisementSerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    pagination_class = LimitOffsetPagination


class AdvertisementViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    pagination_class = LimitOffsetPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = product.objects.all()
    pagination_class = LimitOffsetPagination


class AdvertisementList(generics.ListAPIView):
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Advertisement.objects.filter(user_id=user_id)


@api_view(["GET"])
def health_check(request):
    time.sleep(1)
    return Response({"status": "Ok"}, status.HTTP_200_OK)
