from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
from main.models import MailingMessage, Client, MailingAttempt
from users.models import User
from .serives import get_blog_post_cache


# Create your views here.
def index(request):
    context = {
        'users_len': len(User.objects.all()),
        'messages_len': len(MailingMessage.objects.all()),
        'clients_len': len(Client.objects.all()),
        'mallings_len': len(MailingAttempt.objects.all()),
        'blog_post': get_blog_post_cache()
    }
    return render(request, 'blog/pages/index.html', context)


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/pages/blog_list.html'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/pages/blog_post_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object
