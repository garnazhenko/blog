from django.urls import path



urlpatterns = [
    path('register/', name='account_signup'),
    path('login/', name='account_login'),
    path('logout/', name='account_logout'),
]