from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='book/images')
    summary = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    thoughts = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title