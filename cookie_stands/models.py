from django.contrib.auth import get_user_model
from django.db import models
import random


class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    hourlySales = models.JSONField(default=list, null=True)
    minCustomers = models.IntegerField(default=0)
    maxCustomers = models.IntegerField(default=0)
    avgcookies = models.FloatField(default=0)


    def __str__(self):
        return self.location

    def save(self, *args, **kwargs):

        if not self.pk and not self.hourlySales:
            min = self.minCustomers
            max = self.maxCustomers

            cookies_each_hour = [
                int(random.randint(min, max) * self.avgcookies)
                for _ in range(14)
            ]

            self.hourlySales = cookies_each_hour

        super().save(*args, **kwargs)
