from django.contrib import admin
from .models import Book, Customers, BookRecord
# from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ["id", "title", 'description', 'price', 'count']
    list_display_links = ["id", "title", "description", 'price', 'count']
    ordering = ["-price", "title"]
    search_fields = ["title", "description"]
    filter = ["title"]

@admin.register(Customers)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ["id", "first_name", "last_name", "role"]
    search_fields = ["first_name", "last_name", "role"]

@admin.register(BookRecord)
class BookRecordAdmin(ImportExportModelAdmin):
    list_display = ["id", "customer", 'book', 'returned_date', "create_date"]
    # autocomplete_fields = ["book"]
    search_fields = ["customer", "book"]
    # filter = ["customer"]




