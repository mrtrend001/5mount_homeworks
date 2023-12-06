from django.urls import path

from users import views


urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView),

    path('register/', views.RegisterView),
    path('profile/', views.ProfileView),

    path('confin/', views.UserConfirmationView)
]