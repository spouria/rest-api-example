from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions
from .models import *
from rest_framework_nested.relations import NestedHyperlinkedRelatedField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        #read_only_fields = ['create_date', 'update_date']
        permission_classes = [permissions.DjangoModelPermissions]
        #depth=2

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date']
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        #depth=2


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['book','create_date', 'update_date']
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        #depth=1

class BookDetailSerializer(BookSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, read_only=True,
    view_name='comment-detail')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date']
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GenreDetailSerializer(GenreSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date']
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorDetailSerializer(AuthorSerializer):
    books =  NestedHyperlinkedRelatedField(many=True, read_only=True,
    view_name='author-books-detail',
        parent_lookup_kwargs={'author_pk': 'author__pk'})
