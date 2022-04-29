from django.contrib.auth import views as auth_view
from django.urls import path
from django.urls import reverse_lazy

app_name = 'users'


class UsersPasswordResetView(auth_view.PasswordResetView):
    success_url = reverse_lazy("users:password_reset_done")


class UsersPasswordResetConfirmView(auth_view.PasswordResetConfirmView):
    success_url = reverse_lazy("users:password_reset_complete")


urlpatterns = [
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),

    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),

    path("password_reset/", UsersPasswordResetView.as_view(), name="password_reset"),

    path(
        "reset/<uidb64>/<token>/",
        UsersPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
