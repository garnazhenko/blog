from django.urls import path
from blog.views import PostList
from blog.views import PostDetail
from blog.views import MyPostNew
from blog.views import PostEdit
from blog.views import RegisterUser
from blog.views import LoginUp
from blog.views import logout_user

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', MyPostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('register/', RegisterUser.as_view(), name='register' ),
    path('login/', LoginUp.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
   ]