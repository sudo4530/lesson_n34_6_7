from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name="books"),
    path("books/<int:id>/", BookDetailView.as_view(), name="detail"),
]