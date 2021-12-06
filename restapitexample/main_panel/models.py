from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    create_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    create_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)

class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name='books')
    isbn = models.CharField(max_length=12, unique=True)
    description = models.TextField(max_length=1500)
    create_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{title}".format(title=self.title)


class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    writer = models.ForeignKey(User,related_name='comments',  on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    create_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)
