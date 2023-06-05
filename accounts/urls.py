from django.urls import path
from accounts.views import user_login, user_logout


urlpatterns = [
    path("logout/", user_logout, name="logout"),
    path("login/", user_login, name="login"),
]
