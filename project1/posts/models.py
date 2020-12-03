from django.db import models

from datetime import date

# Create your models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=100)
    name = models.TextField()

    def __str__(self):
        return self.text


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    body_text = models.TextField()
    date_created = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.headline



  


