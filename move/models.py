from django.db import models

class Move(models.Model):
    country_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='move/images/')
    short_description = models.CharField(max_length=500)
    story = models.TextField()
    moved_in = models.DateField(auto_now=False)
    moved_out = models.DateField(auto_now=False)

    def __str__(self):
        return self.city
