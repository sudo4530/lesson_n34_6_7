from django import forms
from .models import Book

class AddBookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "description", "image", "count", "price")



