from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),
    path('forget-pass/', views.ForgetPasswordView.as_view(), name='forget-pass-page'),
    path('reset-pass/<active_code>', views.ResetPasswordView.as_view(), name='reset-pass-page'),
]

