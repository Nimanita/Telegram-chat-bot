from django.db import models

# Create your models here.
class Telegram(models.Model):
    UserId = models.CharField(max_length=25)
    UserFirstName = models.CharField(max_length=200)
    UserLastName = models.CharField(max_length=200)
    UserCount = models.IntegerField(default=1)
    class Meta:
        db_table="Telegram"