from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Author, Genre

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    author_name = serializers.ReadOnlyField(source='author.name')
    genres_names = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        source='genres'
    )


    class Meta:
      model = Book
      fields = ['id', 'title', 'author', 'author_name', 'genres', 'genres_names',
                  'year', 'description', 'language', 'owner', 'status']

        #fields = "__all__"
        #read_only_fields = ["owner"]

class SignupSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True)

      class Meta:
        model = User
        fields = ["username", "email", "password"]

        def create(self, validated_data):
            user = User(
                username=validated_data["username"],
                email=validated_data.get("email")
            )
            user.set_password(validated_data["password"])
            user.save()
            return user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
