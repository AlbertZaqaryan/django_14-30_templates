from django.urls import path
from .views import HomeListView, AboutListView, BlogListView, ContactListView, Post_detailListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('about/', AboutListView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('post/', Post_detailListView.as_view(), name='post'),



]