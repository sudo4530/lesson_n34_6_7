from django.urls import path
from .views import UserLoginView, UserRegisterView, UserListView, UserDetailView, UserSettingsView, LogOut, UserDeleteView

urlpatterns = [
    # auth
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", LogOut.as_view(), name="logout"),
    path("users/", UserListView.as_view(), name="users"),
    path("users/<int:id>/", UserDetailView.as_view(), name="users-detail"),
    path("settings/<int:id>/", UserSettingsView.as_view(), name="settings"),
    path("delete_user/<int:id>/", UserDeleteView.as_view(), name="delete_user"),
]
