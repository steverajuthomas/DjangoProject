from django.urls import path,include
from . import views


urlpatterns = [
    path("test_view/",views.test_view, name="test_view"),
    path("login-page/",views.login_page, name="login-page"),
    path("signup-page/",views.signup_page, name="signup-page"),
    path('all-user-details/',views.all_user_details),
    path('single-user-details/<str:name>/',views.single_user_details),
    path('update-user-details/<str:name>/',views.Update_User_Details),
    path('delete-user-details/<str:email>/',views.Delete_User_Details_by_email),
]
