from django.contrib.auth.models import User

from amidastyle import models
from amidastyle.models import CustomUser, Balance, Advertisement, product, subscription
from rest_framework import serializers


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ["balance"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = ["subscription_chooses", "subscription"]


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ["id", "name", "title", "price", "url", "user_id"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ["id", "name", "title", "price", "user_id"]



class UserSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer(read_only=True)
    product = ProductSerializer(read_only=True)


    class Meta:
        model = CustomUser
        fields = ["id", "name", "user_id", "phone",  "email", "advertisement", "product"]

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)





