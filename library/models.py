from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    price = models.FloatField(default=1)
    count = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)


class Customers(models.Model):
    ROLE = (
        ("student", "S"),
        ("teacher", "T"))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE, default="S")



class BookRecord(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    returned_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_created=True)


