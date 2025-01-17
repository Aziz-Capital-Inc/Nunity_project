from django.urls import path
from .views import register, logout_confirm
from django.contrib.auth.views import *

urlpatterns = [
    path('signup/', register, name='user-register'),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('logout-confirm/', logout_confirm, name='logout-confirm'),  # Corrected the path name
    path('reset-password/', PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password-reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='accounts/password_done.html'), name='password-reset-done'),  # Corrected the template name
    path('password_reset_confirm/', PasswordResetConfirmView.as_view(template_name='accounts/reset.html'), name='password-reset-confirm'),
    path('reset/complete/', PasswordResetCompleteView.as_view(), name='reset-complete')
]
