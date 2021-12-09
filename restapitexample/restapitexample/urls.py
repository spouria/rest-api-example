"""restapitexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from main_panel import views


router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet, basename='author')
router.register(r'book', views.BookViewSet, basename='book')
router.register(r'genre', views.GenreViewSet, basename='genre')
router.register(r'comment', views.CommentViewSet, basename='comment')
router.register(r'user', views.UserViewSet)

author_router = routers.NestedDefaultRouter(router, r'author', lookup='author')
author_router.register(r'book', views.BookViewSet, basename='author-books')

genre_router = routers.NestedDefaultRouter(router, r'genre', lookup='genre')
genre_router.register(r'book', views.BookViewSet, basename='genre-books')

book_router = routers.NestedDefaultRouter(router, r'book', lookup='book')
book_router.register(r'comment', views.CommentViewSet, basename='book-comments')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('', include(author_router.urls)),
    path('', include(genre_router.urls)),
    path('', include(book_router.urls)),

    #Path for Browsable API
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
