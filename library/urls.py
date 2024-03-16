from django.urls import path
from .views import BookListView, BookDetailView, AddBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name="books"),
    path("books/<int:id>/", BookDetailView.as_view(), name="detail"),
    path("add_books/", AddBookView.as_view(), name="add-book"),
]