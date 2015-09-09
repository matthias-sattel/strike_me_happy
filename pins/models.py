from django.db import models
from datetime import datetime

class Pin(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=datetime.now)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title + "\n" + "{:%d, %b %Y}".format(self.creation_date)
