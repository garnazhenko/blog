from django.urls import path
from accounts.views import RegisterUser
from accounts.views import LoginUp
from accounts.views import logout_user

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUp.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]