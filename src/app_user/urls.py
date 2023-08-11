from django.urls import path

from .views import RegisterView, AnotherLoginView, \
    AnotherLogoutView, FeedbackView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", AnotherLoginView.as_view(), name="login"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("logout/", AnotherLogoutView.as_view(), name="logout"),
]