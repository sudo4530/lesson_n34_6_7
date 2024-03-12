from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    price = models.FloatField(default=1)
    count = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)

    def __str__(self):
        return f"{self.id} {self.title} {self.description}"
