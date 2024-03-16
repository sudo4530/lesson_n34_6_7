from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Book
from .forms import AddBookModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            books = Book.objects.all()
            context = {
                "books": books
            }
            return render(request, "library/books.html", context)
        else:
            book = Book.objects.filter(title__icontains=search)
            if not book:
                return HttpResponse("<h3>Not Fount</h3>")
            else:
                context = {
                    "books": book,
                    "search": search
                }
                return render(request, "library/books.html", context)

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, "library/books_detail.html", context={"book": book})

class AddBookView(View):
    def get(self, request):
        form = AddBookModelForm()
        context = {
            "form": form
        }
        return render(request, "library/add_book.html", context)

    def post(self, request):
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        count = request.POST["count"]
        price = request.POST["price"]
        data = {
            "title": title,
            "description": description,
            "image": image,
            "count": count,
            "price": price,
        }
        print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,{data} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        form = AddBookModelForm(data=data)
        if form.is_valid():
            form.save()
            return redirect("books")
        else:
            form = AddBookModelForm()
            context = {
                "form": form
            }
            return render(request, "library/add_book.html", context)



