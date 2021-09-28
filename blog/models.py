from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='blog/images/', blank=True)

    def __str__(self):
        return self.title
