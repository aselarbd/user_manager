from django.urls import path
from server.accounts.views.user_register_post import user_create_view
from server.accounts.views.user_login_post import user_login_view
from knox.views import LogoutView, LogoutAllView


urlpatterns = [
    path('register', user_create_view),
    path('login', user_login_view),
    path('logout', LogoutView.as_view()),
    path('logout-all', LogoutAllView.as_view()),
]
