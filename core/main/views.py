from django.shortcuts import render
from django.views.generic import ListView
from .models import Slider, About1, About2, About3
# Create your views here.


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        slider = Slider.objects.all()
        return render(request, self.template_name, {'slider':slider})


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        about1 = About1.objects.all()
        about2 = About2.objects.all()
        about3 = About3.objects.all()

        return render(request, self.template_name, {'about1':about1,'about2':about2,'about3':about3})



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