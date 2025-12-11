import random
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Book
from .serializers import BookSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken

class Home(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message": "Welcome to the Bookshelf API home page!"})


#from django.http import HttpResponse

#def home(request):
    #return HttpResponse("Welcome to your Bookshelf!")

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
    })

# User Login
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
                })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)  # Fetch user profile
        refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
        return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
    })

# class Home(APIView):
    #def get(self, request):
        #content = {'message': 'Welcome to the cat-collector api home route!'}
        #return Response(content)


class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
# @api_view(['GET'])
# def api_root(request):
#        return Response({
#         "message": "Bookshelf API is running!",
#         "endpoints": {
#             "signup": "/signup/",
#             "books": "/books/",
#         }
    #})

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        owner = self.request.user
        return Book.objects.filter(owner=self.request.user)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecommendedBooksView(APIView):
    def get(self, request):
        books = list(Book.objects.all())
        recommended = random.sample(books, min(3, len(books)))
        serializer = BookSerializer(recommended, many=True)
        return Response(serializer.data)



class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


# class SignupView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SignupSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    
