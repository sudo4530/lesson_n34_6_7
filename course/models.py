from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=50)
    total_course = models.PositiveIntegerField()
    image = models.ImageField(upload_to="course/speciality/")

    def __str__(self):
        return self.title

class CourseRole(models.TextChoices):
    DRAFT = ("Ko'rinmasin", "Ko'rinmasin")
    Publish = ("Ko'rinsin", "ko'rinsin")


class Courses(models.Model):
    title = models.CharField(max_length=100)
    speciality = models.ManyToManyField(Speciality)
    image = models.ImageField(upload_to="course/course/")
    active_students = models.PositiveIntegerField(default=0)
    durection = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    rayting = models.FloatField(default=0.0)
    status = models.CharField(max_length=20, choices=CourseRole.choices, default=CourseRole.Publish)
    create_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.title




