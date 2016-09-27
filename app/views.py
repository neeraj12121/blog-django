from django.views import generic
from app import models


class BlogIndex(generic.ListView):
    queryset = models.Blog.objects.published()
    template_name = "home.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model=models.Blog
    template_name = "post.html"

