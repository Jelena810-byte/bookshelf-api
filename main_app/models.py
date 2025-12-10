from django.db import models
from django.contrib.auth.models import User

# class Genre(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    year = models.IntegerField(default=2000)
    language = models.CharField(max_length=100, default="Unknown")
    #status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_STARTED')

    def __str__(self):
        return self.title



