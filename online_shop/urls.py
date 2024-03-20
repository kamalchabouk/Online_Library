
from django.contrib import admin
from django.urls import path, include
from .views import index, registration_view
from django.contrib.auth import views as auth_views    # new try for password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path("", index, name="index"),
    path("accounts/register/" ,registration_view, name='register'),

    path("reset_password/", auth_views.PasswordResetView.as_view()),  # <-- here is the link to reset - new
]
