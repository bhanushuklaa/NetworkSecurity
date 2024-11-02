from django.db import models

# from django import forms
# Create your models here.


class UserData(models.Model):
    fullname = models.CharField(max_length=20)

    is_active = models.IntegerField(
        default=1,
        blank=True,
        null=True,
        help_text="1->Active, 0->Inactive",
        choices=((1, "Active"), (0, "Inactive")),
    )

    mobileNo = models.CharField(max_length=12)

    email = models.CharField(max_length=40)

    # message = models.TextField()

    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.fullname}, {self.mobileNo}"
