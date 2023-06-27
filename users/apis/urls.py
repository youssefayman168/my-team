from django.urls import path
from .views.login import LoginView
from .views.register import create_admin
from .views.logout import logout

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("register-admin/", create_admin),
    path("logout/", logout),
]
