from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import UserRegisterForm, UserLoginForm

class HomePageView(View):
    def get(self, request):
        return render(request, "users/home.html")

class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "users/login.html", context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("users:home")
        else:
            context = {
                "form": login_form
            }
            return render(request, "users/login.html", context)


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {
            "form": form
        }
        return render(request, "users/register.html", context)

    def post(self, request):
        create_form = UserRegisterForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect("users:login")
        else:
            print("Error")
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)


class UserListView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            users = User.objects.all()
            return render(request, "users/users.html", context={"users": users})
        else:
            user = User.objects.filter(first_name__icontains=search) | User.objects.filter(last_name__icontains=search)
            if not user:
                return HttpResponse("<h1>Not Fount</h1>")
            else:
                context = {
                    "users": user,
                    "search": search
                }
                return render(request, "users/users.html", context)


    def post(self):
        pass


class UserDetailView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, "users/user_detail.html", context={"user": user})

class UserSettingsView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, "users/settings.html", context={"user": user})

    def post(self, request, id):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]

        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save()
        return HttpResponse("<h1>Successfull</h1>")

class ProfileView(View):
    def get(self, request):
        return render(request, "users/profile.html", {"user": request.user})