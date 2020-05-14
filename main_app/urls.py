from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'main_app'

urlpatterns = [
    path('enroll/', views.EnrollView.as_view(), name = 'enroll'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
