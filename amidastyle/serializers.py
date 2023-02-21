from django.contrib.auth.models import User

from amidastyle import models
from amidastyle.models import CustomUser,  Advertisement, product
from rest_framework import serializers




class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ["id", "name", "title", "price", "url", "account_id", "username"]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ["id", "name", "title", "price", "account_id", "username", "contacts"]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "account_id", "subscription"]

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('subscription',)



    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)





