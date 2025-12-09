from django.db import models
from django.contrib.auth.models import User

# Author model: One author → Many books
# class Author(models.Model):
#     name = models.CharField(max_length=150)
#     bio = models.TextField(blank=True)

#     def __str__(self):
#         return self.name

# # Genre model: Many-to-Many with books
# class Genre(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# Book model: Owned by a User, with Author and Genres
# class Book(models.Model):
#     STATUS_CHOICES = [
#         ('NOT_STARTED', 'Not Started'),
#         ('READING', 'Reading'),
#         ('FINISHED', 'Finished'),
#     ]

#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     genres = models.ManyToManyField(Genre, related_name='books', blank=True)
#     year = models.IntegerField()
#     description = models.TextField(blank=True)
#     language = models.CharField(max_length=100)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_STARTED')

#     def __str__(self):
#         return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
