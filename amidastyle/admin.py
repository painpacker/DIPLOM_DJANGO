from django.contrib import admin
from amidastyle.models import  Advertisement, CustomUser,  product



@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('account_id',)
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    pass