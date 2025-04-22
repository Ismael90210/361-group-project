from django.urls import path

from .views import user_login, user_register,course_detail, assignment_detail



urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", user_register, name="signup"),
    path("course/<int:course_id>/", course_detail, name="course_detail"),
    path("assignment/<int:assignment_id>/", assignment_detail, name="assignment_detail"),
]