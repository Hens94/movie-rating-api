from rest_framework import serializers
from django.db.models import Avg
from .models import Movie, Genre, Rating, WatchList

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    rating_avg = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'genre', 'year', 'imdb_id', 'poster_url', 'rating_avg', 'user_created')
        read_only_fields = ('created_at', 'updated_at', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['genre'] = [genre.name for genre in instance.genre.all()]
        return data

    def create(self, validated_data):
        genre_data = validated_data.pop('genre', [])
        movie = Movie.objects.create(**validated_data)
        for genre in genre_data:
            movie.genre.add(genre)
        return movie

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.year = validated_data.get('year', instance.year)
        instance.imdb_id = validated_data.get('imdb_id', instance.imdb_id)
        instance.poster_url = validated_data.get('poster_url', instance.poster_url)
        instance.user_created = validated_data.get('user_created', instance.user_created)
        instance.save()
        instance.genre.clear()
        for genre in genre_data:
            instance.genre.add(genre)
        return instance

class RatingSerializer(serializers.ModelSerializer):
    movie_name = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Rating
        fields = ('id', 'movie', 'movie_name', 'score', 'comment', 'user', 'created_at')        
        read_only_fields = ('movie_name', 'created_at', 'updated_at', )

class WatchListSerializer(serializers.ModelSerializer):
    movie_info = MovieSerializer(read_only=True)

    class Meta:
        model = WatchList
        fields = ('id', 'movie', 'movie_info', 'user', 'created_at')        
        read_only_fields = ('created_at', 'updated_at', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['movie_info'] = MovieSerializer(instance.movie).data
        return data