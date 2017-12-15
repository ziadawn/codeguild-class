from django.db import models

# Create your models here.

# new table for new data!


class Shorturl(models.Model):
    longurl = models.CharField(max_length=500)            # this variable has to match the same one in views
    shorty = models.CharField(max_length=200)

    def __str__(self):              # this controls how things are displayed in the admin panel
        return self.longurl
