from django.urls import path
from .views import Home, BookList, BookDetailView, BookUpdateView, BookDeleteView, CreateUserView, LoginView, VerifyUserView, RecommendedBooksView



urlpatterns = [
    #path('', api_root, name='api_root'),
    path('', Home.as_view, name='home'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    #path('', Home.as_view, name='home'),
    path("books/", BookList.as_view(), name="book_list"),
    path("books/recommended/", RecommendedBooksView.as_view(), name="book-recommended"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),

]


