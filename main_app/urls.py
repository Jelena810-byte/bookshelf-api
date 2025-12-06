from django.urls import path
from .views import (
    api_root,
    BookListCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    SignupView,
)


urlpatterns = [
    path('', api_root, name='api_root'),
    #path('', home, name='home'),
    path("", BookListCreateView.as_view(), name="book_list_create"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("signup/", SignupView.as_view(), name="signup"),
]



