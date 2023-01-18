from django.contrib import admin
from amidastyle.models import Balance, Advertisement, CustomUser, subscription, product


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('user_id',)
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    pass