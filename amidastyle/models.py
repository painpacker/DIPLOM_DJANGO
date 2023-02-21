from django.db import models

class CustomUser(models.Model):
    account_id = models.PositiveIntegerField()
    username = models.CharField(max_length=256)
    subscription = models.PositiveIntegerField()



    def __str__(self):
        return f"{self.username} | {self.account_id}"


class Advertisement(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=256)
    account_id = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    url = models.CharField(max_length=256, blank=True, null=True)
    username = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} | {self.price}"


class product(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=256)
    username = models.CharField(max_length=100)
    contacts = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    account_id = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.name} | {self.price}"







