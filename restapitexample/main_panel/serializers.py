from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['create_date', 'update_date']
        #depth=1
