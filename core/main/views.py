from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)



class BlogListView(ListView):
    template_name = 'blog.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)



class Post_detailListView(ListView):
    template_name = 'post-details.html'

    def get(self, request):
        return render(request, self.template_name)