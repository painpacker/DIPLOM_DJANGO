from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=256)
    advertisement = models.ForeignKey("Advertisement", on_delete=models.CASCADE,  blank=True, default=None, null=True)
    product = models.ForeignKey("product", on_delete=models.CASCADE,  blank=True, default=None, null=True)

    def __str__(self):
        return self.name


class Balance(models.Model):
    User = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.FloatField()


class Advertisement(models.Model):
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    user_id = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.price}"


class product(models.Model):
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} | {self.price}"


class subscription(models.Model):
    User = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subscription_chooses = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]
    subscription = models.CharField(
        max_length=1,
        choices=subscription_chooses,
        default=None,
    )







