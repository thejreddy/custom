from django.urls import path,re_path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_user, name='login'),
    re_path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

     path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"), name ='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"), name ='password_reset_confirm'),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), name ='password_reset_complete'),

]
