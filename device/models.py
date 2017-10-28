from django.db import models

# Create your models here.

class Device(models.Model):
    PK = models.IntegerField(primary_key=True)

    def __str__(self):
        return "< Device - {}>".format(self.PK)

    def __repr__(self):
        return "< Device - {}>".format(self.PK)