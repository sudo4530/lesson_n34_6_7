from django.shortcuts import render
from django.views import View
from .models import Courses, Speciality

class LandingPageView(View):
    def get(self, request):
        specialitys = Speciality.objects.all()
        courses = Courses.objects.all()
        context = {
            "specialitys": specialitys,
            "courses": courses
        }
        return render(request, "landing.html", context)
