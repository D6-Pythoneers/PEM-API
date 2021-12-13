from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, verbose_name="Email Address")
    name = models.CharField(blank=True, null=True, max_length=256)
    role = models.CharField(
        blank=True,
        choices=(
            ("teacher", "Teacher"),
            ("manager", "Manager"),
        ),
        max_length=250,
    )
    school_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=255)
    # password = models.CharField(blank=True, null=True, max_length=256)
    # confirmpassword = models.CharField(blank=True, null=True, max_length=256)
    nid = models.BigIntegerField(blank=True, null=True)
    eid = models.BigIntegerField(blank=True, null=True)
    qualification = models.CharField(
        blank=True,
        choices=(
            ("diploma", "Diploma"),
            ("bachelor", "Bachelor"),
            ("masters", "Masters"),
            ("phd", "PhD"),
        ),
        max_length=256,
        null=True,
    )
    directorate = models.CharField(
        blank=True,
        choices=(
            ("amman1", "Directorate of Amman 1"),
            ("amman2", "Directorate of Amman 2"),
            ("amman3", "Directorate of Amman 3"),
            ("amman4", "Directorate of Amman 4"),
        ),
        max_length=256,
        null=True,
    )

    class Meta:
        db_table = "User"
        verbose_name = "appUser"
        verbose_name_plural = "appUsers"

    def __str__(self):
        return self.username
