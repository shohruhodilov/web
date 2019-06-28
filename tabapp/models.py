from django.db import models
from django.contrib.auth.models import User


class Qurilish(models.Model):
    q_type = models.CharField(max_length=100, null=True)
    servise_name = models.CharField(max_length=100,null=True)
    servise_code = models.CharField(max_length=5, null=True)
    soato = models.CharField(max_length=6, null=True)
    report_month = models.CharField(max_length=6, null=True)
    report_year = models.CharField(max_length=6, null=True)
    last_year = models.CharField(max_length=6,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.q_type


# Create your models here.
