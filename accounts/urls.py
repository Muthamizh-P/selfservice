from django.urls import path, re_path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView

from accounts.views import *

urlpatterns = [
    path('', views.login_index, name="login_index"),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('forgot_username/', views.forgot_username, name="forgot_username"),
    path('check_mail_exist/', views.check_mail_exist, name="check_mail_exist"),
    path('mail_screen/', views.mail_screen, name="mail_screen"),
    path('incorrect/', views.incorrect, name="incorrect"),
    path('profile/', views.profile, name="profile"),
]
