from django.urls import path
from .views import BookListView, BookDetailView, AddBookView, BookSettingsView, BookDeleteView
urlpatterns = [
    path('books/', BookListView.as_view(), name="books"),
    path("books/<int:id>/", BookDetailView.as_view(), name="detail"),
    path("addbooks/", AddBookView.as_view(), name="add-book"),
    path("booksettings/<int:id>/", BookSettingsView.as_view(), name="settings-book"),
    path("bookdelete/<int:id>/", BookDeleteView.as_view(), name="book-delete"),
]