from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, RatingViewSet, WatchListViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('genres', GenreViewSet)
router.register('ratings', RatingViewSet)
router.register('watchlist', WatchListViewSet)

urlpatterns = [
    path('', include(router.urls))
]