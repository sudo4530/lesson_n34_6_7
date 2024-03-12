from django import forms
from django.contrib.auth.models import User

# Base Form
"""class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    def save(self):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()"""


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=56)
    password = forms.CharField(max_length=50)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

