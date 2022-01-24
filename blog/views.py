from .models import Post
from django.views import generic


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


