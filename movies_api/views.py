from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models.functions import Coalesce
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie, Genre, Rating, WatchList
from .serializer import MovieSerializer, GenreSerializer, RatingSerializer, WatchListSerializer
from .pagination import DefaultResultsSetPagination
from django.db.models import Avg

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.annotate(rating_avg=Coalesce(Avg('rating__score'), 0.0)).all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    pagination_class = DefaultResultsSetPagination
    filter_backends = (OrderingFilter,)
    ordering_fields = ('title', 'user_created', 'year', 'rating_avg')

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('-created_at')
    serializer_class = RatingSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'movie']

class WatchListViewSet(viewsets.ModelViewSet):
    queryset = WatchList.objects.all().order_by('-created_at')
    serializer_class = WatchListSerializer
    http_method_names = ['get', 'post', 'delete', 'head']
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'movie']