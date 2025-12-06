from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer, SignupSerializer


#from django.http import HttpResponse

#def home(request):
    #return HttpResponse("Welcome to your Bookshelf!")

from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
@api_view(['GET'])
def api_root(request):
       return Response({
        "message": "Bookshelf API is running!",
        "endpoints": {
            "signup": "/signup/",
            "books": "/books/",
        }
    })

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Users see only their own books
        return Book.objects.filter(owner=self.request.user)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
    permission_classes = [permissions.IsAuthenticated]


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
    
