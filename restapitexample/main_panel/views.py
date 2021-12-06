from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class= UserSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Genre.objects.all()
    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return GenreSerializer
        return GenreDetailSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    #serializer_class = AuthorSerializer

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return AuthorSerializer
        return AuthorDetailSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get_queryset(self):
        if 'author_pk' in self.kwargs:
            return Book.objects.filter(author=self.kwargs['author_pk'])
        if 'genre_pk' in self.kwargs:
            return Book.objects.filter(genre=self.kwargs['genre_pk'])

        return Book.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return BookSerializer
        return BookDetailSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get_queryset(self):
        if 'book_pk' in self.kwargs:
            return Comment.objects.filter(book=self.kwargs['book_pk'])
        return Comment.objects.all()
        
    serializer_class = CommentSerializer
