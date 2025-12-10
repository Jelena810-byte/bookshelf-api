from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  # Ensures the password is hashed correctly
    )
        return user


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
      #fields = ['id', 'title', 'author', 'author_name', 'genres', 'genres_names',
                  #'year', 'description', 'language', 'owner', 'status']
      fields = ['id', 'title', 'author', 'description', 'owner', 'genre', 'year', 'language']
        #fields = "__all__"
        #read_only_fields = ["owner"]

# class SignupSerializer(serializers.ModelSerializer):
#       password = serializers.CharField(write_only=True)

#       class Meta:
#         model = User
#         fields = ["username", "email", "password"]

#         def create(self, validated_data):
#             user = User(
#                 username=validated_data["username"],
#                 email=validated_data.get("email")
#             )
#             user.set_password(validated_data["password"])
#             user.save()
#             return user

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['id', 'name', 'bio']


# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ['id', 'name']
