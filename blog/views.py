from django.contrib.auth.views import LoginView
from .forms import LoginUserForm
from .models import Post
from django.views import generic
from .forms import RegisterUserForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .forms import User
from django.shortcuts import redirect


class PostList(generic.ListView):
    template_name = 'blog/post_list.html'
    queryset = Post.objects.all().order_by('published_date')
    context_object_name = 'posts'


class PostDetail(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'


class MyPostNew(generic.CreateView):
    model = Post
    fields = ['title', 'text', 'author']
    template_name = 'blog/post_edit.html'


class PostEdit(generic.UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    fields = ['title', 'text', 'author']


class RegisterUser(generic.CreateView):
    template_name = 'blog/register.html'
    form_class = RegisterUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUp(LoginView):
    template_name = 'blog/login.html'
    form_class = LoginUserForm


class RegisterDone(generic.ListView):
    template_name = 'blog/register_done.html'
    model = User


def logout_user(request):
    logout(request)
    return redirect('login')