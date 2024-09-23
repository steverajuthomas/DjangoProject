from django.urls import path,include
from . import views

urlpatterns = [
    path("test_view/",views.test_view, name="test_view"),
    path("login-page/",views.login_page, name="login-page"),
    path("signup-page/",views.signup_page, name="signup-page"),
]
