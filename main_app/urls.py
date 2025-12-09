from django.urls import path
from .views import Home, BookListCreateView, BookDetailView, BookUpdateView, BookDeleteView, CreateUserView, LoginView, VerifyUserView


urlpatterns = [
    #path('', api_root, name='api_root'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('', Home.as_view, name='home'),
    path("", BookListCreateView.as_view(), name="book_list_create"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
]


