from django.urls import path
from knox.views import LogoutAllView, LogoutView

from server.accounts.views.user_login_post import user_login_view
from server.accounts.views.user_register_post import user_register_view

urlpatterns = [
    path('register', user_register_view, name='register'),
    path('login', user_login_view, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('logout-all', LogoutAllView.as_view(), name='logout_all'),
]
